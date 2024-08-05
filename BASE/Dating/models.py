from django.db import models
from account.models import User


# Create your models here.

GENDERSELECT=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Both', 'Both'),
    ]
class Genderselect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genderselect = models.CharField(max_length=10,choices=GENDERSELECT,default='B')

    def __str__(self):
        return f"{self.genderselect}"