from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('done/', views.BookingListView.as_view(), name='booked'),
]   