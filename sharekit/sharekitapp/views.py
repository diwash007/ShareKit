from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from .models import Share
from nepse_func import share_data


class ShareListView(LoginRequiredMixin, ListView):
    """ Lists shares on home """
    model = Share
    template_name = 'sharekitapp/home.html'
    context_object_name = 'shares'
    ordering = ['-id']

    def get_queryset(self):
        return Share.objects.filter(
            user=self.request.user
        ).order_by('-id')
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super(ShareListView, self).get_context_data(**kwargs)
        context['share_data'] = share_data
        return context

class ShareDetailView(LoginRequiredMixin, DetailView):
    """ Individual Share details """
    model = Share

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class ShareAddView(LoginRequiredMixin, CreateView):
    """ View to add new shares """
    model = Share
    fields = ['scrip', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShareUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to update existing share details """
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
    """ View to delete an existing share details """
    model = Share
    success_url = '/home'

    def test_func(self):
        share = self.get_object()
        if self.request.user == share.user:
            return True
        return False