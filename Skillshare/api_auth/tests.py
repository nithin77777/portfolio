from django.test import TestCase
from django.urls import reverse
from .models import User
# from .models import User  # Use your custom User model
from django.contrib.auth.hashers import make_password


# Create your tests here.
class  UserLoginTests(TestCase):
    def setUp(self):
        self.url = reverse('login')  # Make sure your login URL is named 'login'
        # Create a test user
        self.user = User.objects.create(
            username='test',
            email='test@example.com',
            password=make_password('root1234')
        )
    
    def test_valid_login(self):
        response = self.client.post(self.url, {
            'username': 'test',
            'password': 'root1234'
        })
        self.assertRedirects(response, reverse('success_view'))

    def test_invalid_password(self):
        response = self.client.post(self.url, {
            'username': 'test',
            'password': 'wrongpass',
            
        })
        self.assertContains(response, "Invalid Password")