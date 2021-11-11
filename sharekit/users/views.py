from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, f'User with username "{username}" doesn\'t exist')
    
    login_form = UserCreateForm()
    context = {
        'form' : login_form
        }
    return render(request, "users/login.html", context)

def register(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account successfully created for {form.cleaned_data.get("username")}')
            return redirect("login")

    context = {
        'form' : form
    }
    return render(request, "users/register.html", context)