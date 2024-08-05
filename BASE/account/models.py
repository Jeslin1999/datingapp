from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES,default='Male')
    images = models.FileField(upload_to='upload/',null=True, blank=True)
    