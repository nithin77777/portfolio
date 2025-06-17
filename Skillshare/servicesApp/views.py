from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Service
# Create your views here.

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
