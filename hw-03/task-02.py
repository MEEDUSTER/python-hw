class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Назва книги: ")
        self.year = int(input("Рік видання: "))
        self.publisher = input("Видавець: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price}")

    def set_price(self, new_price):
        if new_price < 0:
            print("Ціна не може бути від'ємною.")
            return
        self.price = new_price

    def get_price(self):
        return self.price

    def years_since_publication(self, current_year=2026):
        return current_year - self.year


book = Book("Кобзар", 1840, "Просвіта", "поезія", "Тарас Шевченко", 350)
print("Книга:")
book.display()
print("Минуло років від видання:", book.years_since_publication())
book.set_price(320)
print()
print("Після зміни ціни:")
book.display()
