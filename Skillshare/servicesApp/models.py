from django.db import models
# models from other apps
from api_auth.models import User
# Create your models here.

class Service(models.Model):
    # user_booked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_services')
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    # service_book_date = models.DateField(auto_now_add=True, blank=True, null=True):q

    def __str__(self):
        return str(self.service_name)

# Booking model to handle bookings for services
class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service_booked = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.username) + ' booked' + str(self.service_booked) + ' on ' + str(self.booking_date)