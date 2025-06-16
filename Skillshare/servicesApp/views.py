from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Service
# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = 'servicesApp/service_list.html'
    context_object_name = 'services'

    

