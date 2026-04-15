from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout

def enter(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        return redirect("auth", mode='register')
    

def Authentication(request, mode):
    if mode == "register":
        form = forms.UserCreationForm()
        flag = False
    else:
        form = forms.AuthenticationForm()
        flag = True
    return render(request, "Authentication/index.html", {"flag":flag , "form":form})

def register(request):
    form = forms.UserCreationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("main")
    return render(request, "Authentication/index.html", {"flag": False, "form": form})

def user_login(request):
    form = forms.AuthenticationForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("main")
    return render(request, "Authentication/index.html", {"flag": True, "form": form})

def exit(request):
    logout(request)
    return redirect("auth", mode="register")