from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Service, Booking
from .forms import BookingForm
# Create your views here.


def booking_success(request):
    '''
    View to handle the success of a booking.
    It renders a template 'servicesApp/booking_success.html'.
    '''
    return HttpResponse(
        '<h1>Booking Successful!</h1>')

class ServiceListView(ListView):
    model = Service
    template_name = 'servicesApp/service_list.html'
    context_object_name = 'services'

    
class ServiceDetailView(DetailView):
    '''
    View to display the details of a specific service.
    It inherits from DetailView and uses the Service model.
    The template used is 'servicesApp/service_detail.html'.
    The service object uses pk to display each service'.
    '''
    model = Service
    template_name = 'servicesApp/service_details.html'
    context_object_name = 'service'

class BookingCreateView(LoginRequiredMixin,CreateView):
    '''
    View to create a new booking.
    It inherits from CreateView and uses the Booking model.
    The template used is 'servicesApp/booking_form.html'.
    The form is bound to the Booking model.
    '''
    raise_exception = True 
    model = Booking
    form_class = BookingForm
    template_name = 'servicesApp/booking_form.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        '''
        This method is called when the form is valid.
        It sets the username field to the current user and saves the booking.
        '''
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        '''
        This method is called when the form is invalid.
        It returns the form with errors.
        '''
        messages.error(self.request, "There was an error with your booking. Please check the form.")
        return super().form_invalid(form) 



#  Problem to Fix
'''
Booking Create View is not working as expected.
Working even without login.
It should only allow logged-in users to create a booking.
It should redirect to the login page if the user is not logged in.
'''