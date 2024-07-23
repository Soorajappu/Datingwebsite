from django import forms
from accounts.models import User

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
        
class PersonalDetailsForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio-btn gap-5'}))
    
    class Meta:
        model = User
        fields = ['age', 'gender', 'dob', 'hobbies', 'interest', 'qualification', 'profile_pic']
        labels ={
            'age': 'Age',
            'gender': 'Gender',
            'dob': 'Date of Birth',
            'hobbies': 'Hobbies',
            'interest': 'Interests',
            'qualification': 'Qualifications',
            'profile_pic': 'Profile Picture',
        }
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control h-30'}),
            'dob': forms.DateInput(attrs={'class': 'form-control h-30'}),
            'hobbies': forms.Select(attrs={'class': 'form-control h-30'}),
            'interest': forms.Select(attrs={'class': 'form-control h-30'}),
            'qualification': forms.Select(attrs={'class': 'form-control h-30'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control h-30'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name', 'designation', 'location']
        widgets={
            'company_name': forms.TextInput(attrs={'class': 'form-control h-30'}),
            'designation': forms.TextInput(attrs={'class': 'form-control h-30'}),
            'location': forms.TextInput(attrs={'class': 'form-control h-30'}),
        }

class EmployerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name', 'designation', 'location']
        widgets={
            'company_name': forms.TextInput(attrs={'class': 'form-control h-30'}),
            'designation': forms.TextInput(attrs={'class': 'form-control h-30'}),
            'location': forms.TextInput(attrs={'class': 'form-control h-30'}),
        }
        
        
class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['skill_level']