from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    login_state = models.BooleanField(default=False)
    user_created_date = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)  # needed for login to work

    # This tells Django to use 'username' to log in
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # required only for createsuperuser (not needed if you skip superuser)

    def __str__(self):
        return str(self.username)