from django.urls import path
from basic_function import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("subtract", views.subract, name="subtract"),
    path("multiply", views.multiply, name="multiply"),
    path("division", views.division, name="division"),

]

                