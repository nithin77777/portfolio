from django import forms
from .models import Service, Booking

'''
Doing a Form For Booking
This form is used to create a new booking for a service.
It inherits from forms.ModelForm and is bound to the Booking model.
'''

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['username', 'service_booked', 'booking_date']
        widgets = {
            'service_booked': forms.Select(attrs={'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        