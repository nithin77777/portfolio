"""
URL configuration for Skillshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import ServiceListView, ServiceDetailView
# , booking_success, BookingCreateView

urlpatterns = [
    
   
    path('all/',ServiceListView.as_view(), name='services'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    # path('booking/thanks/', booking_success, name='booking_success'),
    # path('booking/', BookingCreateView.as_view(), name='booking'),
]
