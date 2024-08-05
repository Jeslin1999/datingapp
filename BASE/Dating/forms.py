from django.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from .models import Genderselect


class GenderselectForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Both', 'Both'),
    ]
    genderselect = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Genderselect
        fields = ['genderselect']