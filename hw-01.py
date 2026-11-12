def odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


def multiples_of_five(start, end):
    for number in range(start, end + 1):
        if number % 5 == 0:
            yield number


def print_palindromes(start, end):
    palindromes = (
        number
        for number in range(start, end + 1)
        if str(number) == str(number)[::-1]
    )
    for number in palindromes:
        print(number)


start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

if start > end:
    start, end = end, start

print("Непарні числа:")
for number in odd_numbers(start, end):
    print(number)

print("Кратні п'яти:")
for number in multiples_of_five(start, end):
    print(number)

print("Паліндроми:")
print_palindromes(start, end)
