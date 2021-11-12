from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from .models import Share


# @login_required
# def home(request):
#     context = {
#         'shares': request.user.share_set.all()
#     }
#     return render(request, "sharekitapp/home.html", context)

class ShareListView(LoginRequiredMixin, ListView):
    model = Share
    template_name = 'sharekitapp/home.html'
    context_object_name = 'shares'
    ordering = ['-id']

    def get_queryset(self):
        return Share.objects.filter(
            user=self.request.user
        ).order_by('-id')

class ShareDetailView(LoginRequiredMixin, DetailView):
    model = Share

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class ShareAddView(LoginRequiredMixin, CreateView):
    model = Share
    fields = ['scrip', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShareUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Share
    fields = ['scrip', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        share = self.get_object()
        if self.request.user == share.user:
            return True
        return False

class ShareDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Share
    success_url = '/home'

    def test_func(self):
        share = self.get_object()
        if self.request.user == share.user:
            return True
        return False