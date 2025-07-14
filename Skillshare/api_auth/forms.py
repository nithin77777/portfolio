from django import forms

from .models import CustomUser  # importing model 

class SignupModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120,
                               label='Username', 
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(label='Password',
                               max_length=120,min_length=8,
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=120,
        label='Enter Your Email',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))