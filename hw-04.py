from datetime import date


class Book:
    def __init__(self, title, author, year, pages):
        current_year = date.today().year
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Кількість сторінок не може бути від'ємною")
        if not isinstance(year, int) or year < 1 or year > current_year:
            raise ValueError(f"Некоректний рік видання: {year}")
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f"{self.title} — {self.author} ({self.year}), {self.pages} стор."

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year}, {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages

    def __contains__(self, word):
        return str(word).lower() in self.title.lower()

    def __bool__(self):
        return self.pages > 0


book1 = Book("Кобзар", "Тарас Шевченко", 1840, 320)
book2 = Book("Лісова пісня", "Леся Українка", 1911, 180)
book3 = Book("Місто", "Валер'ян Підмогильний", 1928, 280)
book4 = Book("Кобзар", "Тарас Шевченко", 2012, 400)

print("Книги:")
print(book1)
print(book2)
print(book3)
print()
print("repr:", repr(book1))
print("Сторінок у першій книзі:", len(book1))
print("Однакові за назвою та автором:", book1 == book4)
print("book2 коротша за book1:", book2 < book1)
print("Разом сторінок (book1 + book2):", book1 + book2)
print("'пісня' є в назві другої книги:", "пісня" in book2)
print()

library = [book1, book2, book3]
print("Відсортовано за кількістю сторінок:")
for book in sorted(library):
    print(book)

empty = Book("Чернетка", "Невідомий", 2020, 0)
print()
print("Непорожня книга:", bool(book1))
print("Порожня книга (0 стор.):", bool(empty))

try:
    Book("Помилка", "Автор", 3000, 100)
except ValueError as error:
    print("Перевірка року:", error)

try:
    Book("Помилка", "Автор", 2020, -5)
except ValueError as error:
    print("Перевірка сторінок:", error)
