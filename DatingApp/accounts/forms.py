from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from datetime import date


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50,min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'phone_no', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'id': 'password'}),
        }
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not email.endswith('@gmail.com'):
            self.add_error('email',"Email must be a valid Gmail address.")
        if User.objects.filter(email=email).exists():
            self.add_error('email',"A user with that email already exists.")
        return email       
        
    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if phone_no and (len(str(phone_no)) != 10 or not phone_no.isdigit()):
            self.add_error('phone_no', "Phone number must be 10 digits.")
        if User.objects.filter(phone_no=phone_no).exists():
            self.add_error('phone_no',"A user with this phone number already exists.")
        return phone_no
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password',"Passwords do not match")
        return cleaned_data

        
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
        
      
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            return age
        if age < 18:
            self.add_error('age', "Age must be 18 or above.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        dob = cleaned_data.get("dob")

        if dob:
            today = date.today()
            calculated_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age != calculated_age:
                self.add_error('age', "Age and date of birth do not match.")
                self.add_error('dob', "Date of birth and age do not match.")

        return cleaned_data
        
        
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