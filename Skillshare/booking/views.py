from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UserBooking

# Create your views here.

def index(request):
    return render(request, 'booking/index.html')