from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Hobbies(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.CharField(max_length=250)
    
    def __str__(self):
        return self.hobby
    
    
class Interests(models.Model):
    id = models.AutoField(primary_key=True)
    interest = models.CharField(max_length=250)
    
    def __str__(self):
        return self.interest
    
    
class Qualifications(models.Model):
    id = models.AutoField(primary_key=True)
    qualification = models.CharField(max_length=250)
    
    def __str__(self):
        return self.qualification
    
    
class PersonalDetails(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interests, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualifications, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"Personal Details of {self.id}"
    
    
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    
class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class JobSeeker(models.Model):
    id = models.AutoField(primary_key=True)
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)