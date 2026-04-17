from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter, name="enter"),
    path('Authentication/<str:mode>/', views.auth_page, name="auth_page"),
    path('reg/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]