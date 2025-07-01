from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserBooking
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request, 'booking/index.html')


class BookingCreateView(LoginRequiredMixin, CreateView):
    '''
    View to create a new booking.
    '''
    raise_exception = False
    model = UserBooking
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
