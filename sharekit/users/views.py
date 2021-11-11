from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next') or "home")
        messages.error(request, 'Invalid login credentials.')
    
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

@login_required
def logout_user(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    return render(request, "users/profile.html")