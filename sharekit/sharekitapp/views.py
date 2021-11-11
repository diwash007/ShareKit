from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Share


@login_required
def home(request):
    context = {
        'shares': request.user.share_set.all()
    }
    return render(request, "sharekitapp/home.html", context)