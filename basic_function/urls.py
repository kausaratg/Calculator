from django.urls import path
from basic_function import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]


