from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm



class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50,min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'phone_no', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
        
class UserRegisterDetailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age','gender', 'dob', 'highest_qualification', 'hobbies', 'interest', 'smocking_habit',
                  'drinking_habit', 'profile_pic']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=User.GENDER_CHOICES),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'highest_qualification': forms.Select(attrs={'class': 'form-control'}),
            'hobbies': forms.CheckboxSelectMultiple(),
            'interest': forms.Select(attrs={'class': 'form-control'}),
            'smocking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'drinking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class EmploymentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name', 'designation', 'work_location']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'work_location': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class EmploymentJobseekerForm(forms.ModelForm):
    class Meta:
        model = User                            
        fields = ['skill_level']
        widgets = {
            'skill_level': forms.Select(attrs={'class': 'form-control'}),
        }