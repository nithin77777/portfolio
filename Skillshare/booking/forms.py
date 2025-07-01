from django import forms
from .models import Service
from booking.models import UserBooking

'''
Doing a Form For Booking
This form is used to create a new booking for a service.
It inherits from forms.ModelForm and is bound to the Booking model.
'''

class BookingForm(forms.ModelForm):
    class Meta:
        model = UserBooking
        fields = ['username', 'service', 'booking_date']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        