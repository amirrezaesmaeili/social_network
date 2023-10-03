from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterationForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' }))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user :
            raise ValidationError(" this email has been exists ")
        return email
    
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        user = User.objects.filter(username=user_name).exists()
        if user :
            raise ValidationError("this username has been exists")
        return user_name
