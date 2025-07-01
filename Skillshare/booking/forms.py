from django import forms
from .models import UserBooking

class UserBookingForm(forms.ModelForm):
    class Meta:
        model = UserBooking
        fields = ['user', 'service', 'booking_date']
        widgets = {
            'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }

   