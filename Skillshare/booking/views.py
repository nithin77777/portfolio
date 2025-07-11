from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import mail
from django.contrib import messages

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
    template_name = 'booking/booking_form.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('booked')

    def form_valid(self, form):
        try:
            form.instance.username = self.request.user
            response = super().form_valid(form)
            mail.send_mail(
                subject='Booking Confirmation',
                message=f'Your booking for {form.instance.service} on {form.instance.booking_date} was successful.',
                from_email='no-reply@yourdomain.com',
                recipient_list=[self.request.user.email],
                fail_silently=True,
            )
            messages.success(self.request, "Booking created successfully!")
            
            return response
        
        except Exception:
            messages.error(self.request, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your booking. Please check the form.")
        return super().form_invalid(form)


class BookingListView(LoginRequiredMixin, ListView):
    model = UserBooking
    template_name = 'booking/user_bookings.html'  # <-- update this
    context_object_name = 'bookings'

    def get_queryset(self):
        return UserBooking.objects.filter(username=self.request.user)