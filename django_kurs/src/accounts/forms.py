from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts import models 
from . import models



class ProfileForm(forms.Form):
    class Meta:
        model = models.Customer
        fields = (
            'phone',
            'city',
            'address',
            'index')



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            'username', 
            'password', 
            'first_name',
            'last_name', 
            'email')