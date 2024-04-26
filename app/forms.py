from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerProfile, ExecutorProfile

class CustomerRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    contact_info = forms.CharField(max_length=100)
    experience = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'contact_info', 'experience']

class ExecutorRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    contact_info = forms.CharField(max_length=100)
    experience = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'contact_info', 'experience']