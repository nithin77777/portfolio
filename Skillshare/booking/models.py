from django.db import models
from api_auth.models import CustomUser
from servicesApp.models import Service

# Create your models here.

class UserBooking(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking by {self.user} for {self.service} on {self.booking_date}"


