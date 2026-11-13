def show_line(symbol, function_to_call):
    function_to_call(symbol)


def horizontal_line(symbol):
    print(symbol * 20)


def vertical_line(symbol):
    for _ in range(10):
        print(symbol)


symbol = input("Введіть символ для лінії: ")
choice = input("Яку лінію відобразити? (h - горизонтальну, v - вертикальну): ").lower()

if choice == "h":
    show_line(symbol, horizontal_line)
elif choice == "v":
    show_line(symbol, vertical_line)
else:
    print("Невірний вибір.")
