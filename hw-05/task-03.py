class Money:
    def __init__(self, whole=0, cents=0, currency="грн"):
        self.currency = currency
        self.set_values(whole, cents)

    def set_values(self, whole, cents):
        total = whole * 100 + cents
        if total < 0:
            print("Сума не може бути від'ємною.")
            return
        self.whole = total // 100
        self.cents = total % 100

    def display(self):
        print(f"{self.whole}.{self.cents:02d} {self.currency}")

    def __str__(self):
        return f"{self.whole}.{self.cents:02d} {self.currency}"


class Product(Money):
    def __init__(self, name, whole=0, cents=0, currency="грн"):
        super().__init__(whole, cents, currency)
        self.name = name

    def reduce_price(self, amount):
        discount = int(round(amount * 100))
        total = self.whole * 100 + self.cents - discount
        if total < 0:
            print("Ціна не може стати від'ємною.")
            return
        self.set_values(0, total)

    def display(self):
        print(f"{self.name}: {self.whole}.{self.cents:02d} {self.currency}")

    def __str__(self):
        return f"{self.name}: {self.whole}.{self.cents:02d} {self.currency}"


money = Money(10, 50)
print("Сума:")
money.display()
money.set_values(5, 150)
print("Після задання 5 грн 150 коп.:")
money.display()
print()

product = Product("Кава", 12, 99)
print("Товар:")
product.display()
product.reduce_price(2.50)
print("Після знижки 2.50:")
product.display()
product.reduce_price(20)
