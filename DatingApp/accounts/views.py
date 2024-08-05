from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView,TemplateView,FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'dating/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
    
    
class UserCreateView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:register_detail')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.set_password(user.password)
        user.save()
        login(self.request, user)
        return redirect(self.success_url)
    
    
class RegisterBasicDetailView(LoginRequiredMixin, FormView):
    template_name = 'accounts/register_detail.html'
    form_class = UserRegisterDetailForm
    success_url = reverse_lazy('accounts:employment')
    
    def get_form_kwargs(self):
        return {'instance': self.request.user, 'data': self.request.POST, 'files': self.request.FILES}
    
    
    def get_initial(self) -> dict[str, any]:
        return super().get_initial()
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('accounts:home')
    
    
    
class IndexView(TemplateView):
    template_name = 'accounts/index.html'
    
    
class EmploymentView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/employment.html'
    
    
class EmployerDetailView(LoginRequiredMixin, FormView):
    template_name = 'accounts/employer.html'
    form_class = EmploymentForm
    success_url = reverse_lazy('accounts:relationship')
    
    def get_form_kwargs(self):
        return {'instance': self.request.user, 'data': self.request.POST}
    
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    
    
class JobSeekerDetailView(LoginRequiredMixin, FormView):
    template_name = 'accounts/jobseeker.html'
    form_class = EmploymentJobseekerForm
    success_url = reverse_lazy('accounts:relationship')
    
    def get_form_kwargs(self):
        return {'instance': self.request.user, 'data': self.request.POST}
    
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    

class RelationshipView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/relationship.html'
    
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'accounts:login'