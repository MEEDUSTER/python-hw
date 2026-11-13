import json


class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class JsonMixin:
    def to_json(self):
        return json.dumps(
            {"name": self.name, "price": self.price},
            ensure_ascii=False
        )


class DiscountMixin:
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Відсоток знижки має бути від 0 до 100.")
            return
        self.price = self.price * (1 - percent / 100)
        self.log(f"Застосовано знижку {percent}%. Нова ціна: {self.price} грн")
        return self.price


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} грн"


class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    pass


product = ProductManager("Ноутбук", 1000)
print("До знижки:", product)
print("JSON:", product.to_json())
product.apply_discount(15)
print("Після знижки 15%:", product)
print("Ціна:", product.price, "грн")
print("JSON:", product.to_json())

print()
print("ProductManager.mro():")
for item in ProductManager.mro():
    print("-", item)

print()
print(
    "Пояснення: Python шукає методи в такому порядку — спочатку сам клас "
    "ProductManager, далі батьківські класи зліва направо: Product, "
    "LoggingMixin, JsonMixin, DiscountMixin, і наприкінці базовий object. "
    "Тому apply_discount береться з DiscountMixin, а log — з LoggingMixin."
)
