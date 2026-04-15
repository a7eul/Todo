from django.urls import path
from . import views

urlpatterns = [
    path('',views.enter, name="enter"),
    path('Authentication/<str:mode>/', views.Authentication, name="auth"),
    path('reg/', views.register, name="reg"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.exit, name="logout"),
]