from django import forms
from .models import User, PersonalDetails, ProfileMultPic, Videos, Hobbies, Interests, Employee, Employer, JobSeeker

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
        
class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['age', 'dob', 'hobbies', 'interest', 'qualification', 'profile_pic']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'hobbies': forms.Select(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'interest': forms.Select(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'qualification': forms.Select(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = ProfileMultPic
        fields = ['image']
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['video']
        widgets={
            'video': forms.FileInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['company_name', 'designation', 'location']
        widgets={
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
        }

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'designation', 'location']
        widgets={
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style':'height: 30px;', 'style':'margin-bottom: -8px;'}),
        }
        
        
class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['skill_level']