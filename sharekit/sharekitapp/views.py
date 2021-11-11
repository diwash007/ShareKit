from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Share


def home(request):
    context = {
        'shares': Share.objects.all()
    }
    return render(request, "sharekitapp/home.html", context)