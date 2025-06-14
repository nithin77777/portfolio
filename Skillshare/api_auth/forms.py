from django import forms

from .models import User  # importing model 

class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'  # Or specify fields like 
        fields = ['username', 'email', 'password']  # Specify the fields you want to include in the form
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password': 'Password',
        }