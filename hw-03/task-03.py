from datetime import datetime, date


class Stadium:
    def __init__(self, name="", opening_date=None, country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date if opening_date is not None else date(1900, 1, 1)
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Назва стадіону: ")
        raw_date = input("Дата відкриття (рррр-мм-дд): ")
        self.opening_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
        self.country = input("Країна: ")
        self.city = input("Місто: ")
        self.capacity = int(input("Місткість: "))

    def display(self):
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def set_capacity(self, new_capacity):
        if new_capacity < 0:
            print("Місткість не може бути від'ємною.")
            return
        self.capacity = new_capacity

    def get_capacity(self):
        return self.capacity

    def age(self, current_year=2026):
        return current_year - self.opening_date.year


stadium = Stadium("Олімпійський", date(1923, 8, 12), "Україна", "Київ", 70050)
print("Стадіон:")
stadium.display()
print("Вік стадіону:", stadium.age(), "р.")
stadium.set_capacity(65000)
print()
print("Після зміни місткості:")
stadium.display()
