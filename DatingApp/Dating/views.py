from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreateForm,PersonalDetailsForm,EmployeeForm,EmployerForm,JobSeekerForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# Create your views here.
class RelationshipView(TemplateView):
    template_name = 'dating/relationship.html'
    
    
class HomeView(TemplateView):
    template_name = 'dating/home.html'
    
    
class EmploymentView(TemplateView):
    template_name = 'dating/employment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = EmployeeForm()
        context['employer_form'] = EmployerForm()
        context['job_seeker_form'] = JobSeekerForm()
        return context


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'dating/user_create.html'
    
    
class DetailCreateView(TemplateView):
    form_class = PersonalDetailsForm
    template_name = 'dating/personal_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_form'] = PersonalDetailsForm()
        return context
