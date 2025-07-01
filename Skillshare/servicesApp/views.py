from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

# from .models import Service, Booking
# from .forms import BookingForm
from .models import Service

def booking_success(request):
    '''
    View to handle the success of a booking.
    It renders a template 'servicesApp/booking_success.html'.
    '''
    try:
        return HttpResponse('<h1>Booking Successful!</h1>')
    except Exception:
        return HttpResponse('<h1>Something went wrong. Please try again later.</h1>', status=500)

class ServiceListView(ListView):
    model = Service
    template_name = 'servicesApp/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    '''
    View to display the details of a specific service.
    '''
    model = Service
    template_name = 'servicesApp/service_details.html'
    context_object_name = 'service'

"""
class BookingCreateView(LoginRequiredMixin, CreateView):
    '''
    View to create a new booking.
    '''
    raise_exception = False
    model = Booking
    form_class = BookingForm
    template_name = 'servicesApp/booking_form.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        try:
            form.instance.username = self.request.user
            return super().form_valid(form)
        except Exception:
            messages.error(self.request, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your booking. Please check the form.")
        return super().form_invalid(form)

"""