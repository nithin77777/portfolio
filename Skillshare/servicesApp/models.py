from django.db import models
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