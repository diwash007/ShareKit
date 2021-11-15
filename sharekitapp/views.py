from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .models import Share, Demat
from .forms import Ipo
from nepse_func import share_data, get_ipo_result


###### Landing page view ######
def index(request):
    return render(request, "sharekitapp/index.html")
    
###### Share views ######
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
    template_name = 'sharekitapp/delete.html'

    def test_func(self):
        share = self.get_object()
        if self.request.user == share.user:
            return True
        return False

###### Demat views ######
class DematListView(LoginRequiredMixin, ListView):
    """ Lists demats on ipo """
    model = Demat
    template_name = 'sharekitapp/ipo.html'
    context_object_name = 'demats'
    ordering = ['-id']

    def get_queryset(self):
        return Demat.objects.filter(
            user=self.request.user
        ).order_by('-id')
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super(DematListView, self).get_context_data(**kwargs)
        context['share_data'] = share_data
        context['form'] = Ipo()
        return context

class DematAddView(LoginRequiredMixin, CreateView):
    """ View to add new demat account """
    model = Demat
    fields = ['boid', 'name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DematUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to update existing demat details """
    model = Demat
    fields = ['boid', 'name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        demat = self.get_object()
        if self.request.user == demat.user:
            return True
        return False

class DematDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ View to delete an existing demat details """
    model = Demat
    success_url = '/ipo'
    template_name = 'sharekitapp/delete.html'

    def test_func(self):
        demat = self.get_object()
        if self.request.user == demat.user:
            return True
        return False

###### IPO ######
def ipo_check(request):
    if request.method == "POST":
        form = Ipo(request.POST)
        if form.is_valid():
            company = form.cleaned_data["company"]
            result = get_ipo_result(request, company)
            return render(request, "sharekitapp/ipo-check.html", {'result': result})
    return redirect("ipo")
    
