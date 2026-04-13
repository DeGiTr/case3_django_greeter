from django.urls import path

from .views import home


app_name = "greetings"

urlpatterns = [
    path("", home, name="home"),
]
