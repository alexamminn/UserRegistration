from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import *

class forms_user_registration(UserCreationForm):
    email = forms.EmailField(help_text='name@example.com')
    class Meta:
        model = models_user_registration
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class forms_login(forms.ModelForm):
    email = forms.EmailField(help_text='name@example.com')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models_user_registration
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Email and password do not match!')
            
