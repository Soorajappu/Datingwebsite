from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import UserProfileForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from accounts.models import User

# Create your views here.    

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'dating/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('dating:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    