from django import forms
from accounts.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_no', 'email', 'age', 'gender', 'dob', 'highest_qualification', 'hobbies', 'interest', 'smocking_habit',
                  'drinking_habit', 'profile_pic', 'company_name', 'designation', 'work_location', 'skill_level', 'reels', 'profile_images']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=User.GENDER_CHOICES),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'highest_qualification': forms.Select(attrs={'class': 'form-control'}),
            'hobbies': forms.CheckboxSelectMultiple(),
            'interest': forms.Select(attrs={'class': 'form-control'}),
            'smocking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'drinking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'work_location': forms.TextInput(attrs={'class': 'form-control'}),
            'skill_level': forms.Select(attrs={'class': 'form-control'}),   
            'reels': forms.FileInput(attrs={'class': 'form-control'}),
            'profile_images': forms.FileInput(attrs={'class': 'form-control'}),
        }