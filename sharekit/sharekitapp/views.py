from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    
    login_form = UserCreateForm()
    context = {
        'form' : login_form
        }
    return render(request, "sharekitapp/index.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    register_form = UserCreateForm()
    context = {
        'form' : register_form
    }
    return render(request, "sharekitapp/register.html", context)

def home(request):
    return render(request, "sharekitapp/home.html")