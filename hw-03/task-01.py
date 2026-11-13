class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель: ")
        self.year = int(input("Рік випуску: "))
        self.manufacturer = input("Виробник: ")
        self.engine_volume = float(input("Об'єм двигуна (л): "))
        self.color = input("Колір: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price}")

    def set_price(self, new_price):
        if new_price < 0:
            print("Ціна не може бути від'ємною.")
            return
        self.price = new_price

    def get_price(self):
        return self.price

    def change_color(self, new_color):
        self.color = new_color

    def age(self, current_year=2026):
        return current_year - self.year


car = Car("Camry", 2020, "Toyota", 2.5, "чорний", 25000)
print("Автомобіль:")
car.display()
print("Вік автомобіля:", car.age(), "р.")
car.change_color("білий")
car.set_price(23000)
print()
print("Після змін:")
car.display()
