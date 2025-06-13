from django.db import models

# Create your models here.

class User(models.Model):
    """
    Represents a user in the Skillshare application.
    
    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return str(self.username) + "is the created username"
    
    