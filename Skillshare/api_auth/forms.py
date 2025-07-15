from django import forms

from .models import CustomUser  # importing model


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'  # Or specify fields like
        # Specify the fields you want to include in the form
        fields = ['username', 'email', 'password']
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
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label='Password',
                               max_length=120, min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class UpdatePasswordForm(forms.Form):
    '''
    This form is used to update the user's password after login.
    '''
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your old password',
               'class': 'form-control'}
    ))
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm your new password',
               'class': 'form-control'}
    ))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm your new password',
               'class': 'form-control'}
    ))
