from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from api_auth.models import CustomUser as User
from .models import Service
from .forms import ServiceCreateForm

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


class ServiceCreateView(LoginRequiredMixin, FormView):
    '''
    View to create a new service.
    Only accessible to logged-in users.
    '''
    form_class = ServiceCreateForm
    template_name = 'servicesApp/create_service_form.html'
    fields = ['service_name', 'service_description', 'service_price']
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        '''
        This method is called when the form is valid.
        It sets the username field to the current user and saves the booking.
        '''
        user = User.objects.get(username=self.request.user.username)
        if not user.login_state:
            messages.error(self.request, "You need to be logged in to book a service.")
            return super().form_invalid(form)
        # form.instance.username = self.request.user

        # return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     '''
    #     This method is called when the form is invalid.
    #     It returns the form with errors.
    #     '''
    #     messages.error(self.request, "There was an error with your booking. Please check the form.")
    #     return super().form_invalid(form) 

        service_name = form.cleaned_data['service_name']
        service_description = form.cleaned_data['service_description']
        service_price = form.cleaned_data['service_price']

        
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            
            service = Service.objects.create(
            service_name=service_name,
            service_description=service_description,
            service_price=service_price
        )
            return super().form_valid(form)
        else:
            messages.error(self.request, "You do not have permission to create a service.")
            return super().form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the service. Please check the form and try again.')
        return super().form_invalid(form)
    
