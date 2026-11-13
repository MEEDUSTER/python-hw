from django.db import models


class Contact(models.Model):
    first_name = models.CharField("Ім'я", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Контактний телефон", max_length=30)
    notes = models.TextField("Примітки", blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
