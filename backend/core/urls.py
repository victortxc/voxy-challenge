from django.urls import path

from core import views

urlpatterns = [
    path("", views.CountNumberOfWords.as_view(), name="count-number-of-words"),
]
