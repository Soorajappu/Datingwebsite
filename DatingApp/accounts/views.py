from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from .forms import UserCreateForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'accounts/home.html'
    
    
class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/register.html'