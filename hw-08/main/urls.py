from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news, name="news"),
    path("news/<path:extra>/", views.news),
    path("management/", views.management, name="management"),
    path("management/<path:extra>/", views.management),
    path("facts/", views.facts, name="facts"),
    path("facts/<path:extra>/", views.facts),
    path("contacts/", views.contacts, name="contacts"),
    path("contacts/<path:extra>/", views.contacts),
    path("history/people/", views.history_people, name="history_people"),
    path("history/people/<path:extra>/", views.history_people),
    path("history/photos/", views.history_photos, name="history_photos"),
    path("history/photos/<path:extra>/", views.history_photos),
    path("history/", views.history, name="history"),
    path("history/<path:extra>/", views.history),
]
