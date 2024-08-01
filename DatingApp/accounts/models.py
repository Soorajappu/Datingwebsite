from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Hobbies(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.hobby
    
    
class Interests(models.Model):
    id = models.AutoField(primary_key=True)
    interest = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.interest
    
    
class Qualifications(models.Model):
    id = models.AutoField(primary_key=True)
    qualification = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.qualification
    
    
class Designation(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.designation
    
    
class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    USER_TYPE_CHOICES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    ]
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    highest_qualification = models.ForeignKey(to=Qualifications, on_delete=models.CASCADE, null=True)
    hobbies = models.ManyToManyField(to=Hobbies, null=True)
    interest = models.ForeignKey(to=Interests, on_delete=models.CASCADE, null=True)
    smocking_habit = models.BooleanField(default=False)
    drinking_habit = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    company_name = models.CharField(max_length=100, null=True)
    designation = models.ForeignKey(to=Designation, on_delete=models.CASCADE, null=True)
    work_location = models.CharField(max_length=100, null=True)
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    @property
    def is_employer(self):
        return self.company_name is None and self.designation is None and self.work_location is None

    
# class UserHobbies(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(to=User)
#     hobby = models.ForeignKey(to=Hobbies)