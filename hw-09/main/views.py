from datetime import date, timedelta

from django.shortcuts import render

from .forms import LoginForm, NumbersForm, ProgrammerDayForm, RegisterForm

USERS = {
    "admin": {"password": "admin123", "role": "адміністратор"},
    "user": {"password": "user123", "role": "користувач"},
}

WEEKDAYS = [
    "понеділок",
    "вівторок",
    "середа",
    "четвер",
    "п’ятниця",
    "субота",
    "неділя",
]

MONTHS = {
    9: "вересня",
}


def index(request):
    return render(request, "main/index.html", {"page": "index"})


def login_view(request):
    message = None
    ok = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            account = USERS.get(username)
            if account and account["password"] == password:
                ok = True
                message = (
                    f"Вітаємо, {username}! "
                    f"Ваш рівень доступу: {account['role']}."
                )
            else:
                message = "Неправильні параметри входу."
    else:
        form = LoginForm()
    return render(
        request,
        "main/login.html",
        {"form": form, "message": message, "ok": ok, "page": "login"},
    )


def numbers_view(request):
    result = None
    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["number1"]
            b = form.cleaned_data["number2"]
            c = form.cleaned_data["number3"]
            operation = form.cleaned_data["operation"]
            if operation == "min":
                result = f"Мінімум із трьох: {min(a, b, c)}"
            elif operation == "max":
                result = f"Максимум із трьох: {max(a, b, c)}"
            else:
                average = (a + b + c) / 3
                result = f"Середнє арифметичне із трьох: {average}"
    else:
        form = NumbersForm()
    return render(request, "main/numbers.html", {"form": form, "result": result, "page": "numbers"})


def register_view(request):
    data = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            gender_labels = {"female": "Жіноча", "male": "Чоловіча"}
            data = {
                "Ім'я": form.cleaned_data["first_name"],
                "Прізвище": form.cleaned_data["last_name"],
                "Вік": form.cleaned_data["age"],
                "Email": form.cleaned_data["email"],
                "Стать": gender_labels[form.cleaned_data["gender"]],
                "Адреса для доставки": form.cleaned_data["address"],
                "Підписка на новини": (
                    "Так" if form.cleaned_data["subscribe"] else "Ні"
                ),
            }
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form, "data": data, "page": "register"})


def programmer_day(year):
    day = date(year, 1, 1) + timedelta(days=255)
    weekday = WEEKDAYS[day.weekday()]
    month = MONTHS[day.month]
    return f"{day.day} {month} ({weekday})"


def programmer_day_view(request):
    result = None
    if request.method == "POST":
        form = ProgrammerDayForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            result = f"День програміста у {year} році: {programmer_day(year)}."
    else:
        form = ProgrammerDayForm()
    return render(
        request,
        "main/programmer_day.html",
        {"form": form, "result": result, "page": "programmer_day"},
    )
