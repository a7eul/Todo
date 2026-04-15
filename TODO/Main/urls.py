from django.urls import path
from .models import User, Task
from .core_logic import get_statistical
from django.http import JsonResponse
from . import views



urlpatterns = [
    path("main/", views.main , name="main"),
    path("main/create/", views.create, name="create"),
    path("main/update/", views.update, name="update"),
]