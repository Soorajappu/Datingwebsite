from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Hobbies(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
class Interests(models.Model):
    id = models.AutoField(primary_key=True)
    interest = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
class Qualifications(models.Model):
    id = models.AutoField(primary_key=True)
    qualification = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
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
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interests, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualifications, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    slug = models.SlugField(unique=True, blank=True, null=True)