from django import forms
from .models import Service

class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description', 'service_price']
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'form-control'}),
            'service_description': forms.Textarea(attrs={'class': 'form-control'}),
            'service_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
