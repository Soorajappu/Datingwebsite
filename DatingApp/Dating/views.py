from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreateForm,PersonalDetailsForm,EmployeeForm,EmployerForm,JobSeekerForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# Create your views here.    
class HomeView(TemplateView):
    template_name = 'dating/home.html'
    
    
def user_profile_view(request):
    user_type = request.user.type  # Assuming the user is logged in and `request.user` is an instance of your `User` model

    context = {
        'user_type': user_type,
        'employee_form': EmployeeForm(),
        'employer_form': EmployerForm(),
        'job_seeker_form': JobSeekerForm(),
    }

    return render(request, 'your_template.html', context)


class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('dating:details_create')
    template_name = 'dating/user_create.html'
    
    
class DetailCreateView(TemplateView):
    form_class = PersonalDetailsForm
    success_url = reverse_lazy('dating:employment')
    template_name = 'dating/personal_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_form'] = PersonalDetailsForm()
        return context


class EmploymentView(TemplateView):
    success_url = reverse_lazy('dating:relationship')
    template_name = 'dating/employment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = EmployeeForm()
        context['employer_form'] = EmployerForm()
        context['job_seeker_form'] = JobSeekerForm()
        return context
    
    
class RelationshipView(TemplateView):
    success_url = reverse_lazy('dating:home')
    template_name = 'dating/relationship.html'