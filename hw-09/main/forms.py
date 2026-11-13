from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Логін", max_length=50)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class NumbersForm(forms.Form):
    number1 = forms.FloatField(label="Перше число")
    number2 = forms.FloatField(label="Друге число")
    number3 = forms.FloatField(label="Третє число")
    operation = forms.ChoiceField(
        label="Що знайти",
        choices=[
            ("min", "Мінімум із трьох"),
            ("max", "Максимум із трьох"),
            ("avg", "Середнє арифметичне із трьох"),
        ],
        widget=forms.RadioSelect,
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Ім'я", max_length=50)
    last_name = forms.CharField(label="Прізвище", max_length=50)
    age = forms.IntegerField(label="Вік", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(
        label="Стать",
        choices=[
            ("female", "Жіноча"),
            ("male", "Чоловіча"),
        ],
        widget=forms.RadioSelect,
    )
    address = forms.CharField(
        label="Адреса для доставки товару",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    subscribe = forms.BooleanField(
        label="Бажаєте підписатися на новини нашого інтернет-магазину?",
        required=False,
    )


class ProgrammerDayForm(forms.Form):
    year = forms.IntegerField(label="Рік", min_value=1, max_value=9999)
