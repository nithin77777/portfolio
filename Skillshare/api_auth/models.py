from django.db import models
# Importing User Manager
from django.contrib.auth.base_user import BaseUserManager
# Importing AbstractBaseUser and PermissionsMixin for custom user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Importing timezone for setting default date/time
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a user with an email, username, and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('login_state', False)
        extra_fields.setdefault('user_created_date', timezone.now())
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password    
        user.save(using=self._db)
        return user

    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email, username, and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('login_state', False)
        extra_fields.setdefault('user_created_date', timezone.now())
        
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        return self.create_user(username, email, password, **extra_fields)
        


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    
   # personal information fields for the user
    is_active = models.BooleanField(default=True)  # needed for login to work
    login_state = models.BooleanField(default=False)
    user_created_date = models.DateTimeField(default=timezone.now)

# Permissions and status fields for superuser
    is_staff = models.BooleanField(default=False)  # allows access to admin site
    is_superuser = models.BooleanField(default=False)  # grants all permissions
    is_admin = models.BooleanField(default=False)  # custom field for admin status

    # This tells Django to use 'username' to log in
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # required only for createsuperuser (not needed if you skip superuser)

    objects = CustomUserManager()  # using the custom user manager
    def __str__(self):
        return str(self.username)
    





    
