from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse  

def redirect_to_auth(mode):
    return redirect(reverse('auth_page', kwargs={'mode': mode}))

def enter(request):
    
    if request.user.is_authenticated:
        return redirect("main")
    return redirect_to_auth("register")  
def auth_page(request, mode="register"):
   
    if mode == "register":
        form = UserCreationForm()
        flag = False  
    else:
        form = AuthenticationForm(request) 
        flag = True
    return render(request, "Authentication/index.html", {"flag": flag, "form": form})

def register(request):
    if request.method != "POST":
        return redirect_to_auth("register")
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)  
    return render(request, "Authentication/index.html", {"flag": False, "form": form})

def user_login(request):
    if request.method != "POST":
        return redirect_to_auth("login")
    
    form = AuthenticationForm(request, data=request.POST) 
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("main")
    return render(request, "Authentication/index.html", {"flag": True, "form": form})

def user_logout(request):  
    logout(request)
    return redirect_to_auth("register")