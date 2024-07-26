from django import forms
from accounts.models import User



class UserCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control h-35'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'age', 'gender', 'dob', 'highest_qualification',  'hobbies',
                  'interest', 'smocking_habit', 'drinking_habit', 'profile_pic', 'types', 'company_name', 'designation', 'location',
                  'skill_level']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control h-35'}),
            'email': forms.EmailInput(attrs={'class': 'form-control h-35'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control h-35'}),
            'age': forms.NumberInput(attrs={'class': 'form-control h-35'}),
            'gender': forms.RadioSelect(choices=User.GENDER_CHOICES ,attrs={'class': 'radio-btn gap-5'}),
            'dob': forms.DateInput(attrs={'class': 'form-control h-30'}),
            'highest_qualification': forms.Select(attrs={'class': 'form-control h-35'}),
            'hobbies': forms.Select(attrs={'class': 'form-control h-35'}),
            'interest': forms.Select(attrs={'class': 'form-control h-35'}), 
            'smocking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'drinking_habit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control h-35'}),
            'types': forms.Select(attrs={'class': 'form-control h-35', 'id': 'id_type'}),  # Ensure 'id_type' is set here
            'company_name': forms.TextInput(attrs={'class': 'form-control h-35', 'id': 'id_company_name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control h-35', 'id': 'id_designation'}),
            'location': forms.TextInput(attrs={'class': 'form-control h-35', 'id': 'id_location'}),
            'skill_level': forms.Select(attrs={'class': 'form-control h-35', 'id': 'id_skill_level'}),
        }