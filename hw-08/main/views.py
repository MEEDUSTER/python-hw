from django.shortcuts import render


def home(request, extra=None):
    return render(request, "main/home.html", {"section": "home"})


def news(request, extra=None):
    return render(request, "main/news.html", {"section": "news"})


def management(request, extra=None):
    return render(request, "main/management.html", {"section": "management"})


def facts(request, extra=None):
    return render(request, "main/facts.html", {"section": "facts"})


def contacts(request, extra=None):
    return render(request, "main/contacts.html", {"section": "contacts"})


def history(request, extra=None):
    return render(request, "main/history.html", {"section": "history"})


def history_people(request, extra=None):
    return render(request, "main/history_people.html", {"section": "history_people"})


def history_photos(request, extra=None):
    return render(request, "main/history_photos.html", {"section": "history_photos"})
