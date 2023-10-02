from django import forms

class RegisterationForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()