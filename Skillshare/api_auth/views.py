from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth  import login, logout
# from django.contrib.auth import lo
from django.utils import timezone
# Assuming User model is defined in models.py
from .models import CustomUser
# Assuming forms are defined in forms.py
from .forms import SignupModelForm, LoginForm

# Create your views here.


def index(req):
    """
    Render the index page.
    """

    return HttpResponse(
        """<h1>Hello, world! This is the index page. </h1>"""
    )


def success_view(request):
    """
    Render the success page after a successful operation.

    This view is typically used to confirm that a user has been created or updated successfully.
    """
    response = HttpResponse("<h1>Success! User has been created/updated.</h1>")
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    return response


class SignupView(CreateView):
    """
    View for handling user-related operations.

    This view supports creating, listing, updating, and deleting users.
    """

    template_name = 'signup_form.html'
    form_class = SignupModelForm
    model = CustomUser

    # Redirect to index after successful operation
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        # Assuming you have a function to hash passwords
        user.password = make_password(user.password)
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    """
    View for handling user login.

    This view displays the details of a user.
    """

    form_class = LoginForm
    template_name = 'login_form.html'
    success_url = reverse_lazy('services')  # Redirect to services page after login

    def form_invalid(self, form):
        """
        Handle the login form submission.

        This method checks the credentials and logs in the user if they are valid.
        """
        response = super().form_invalid(form)
        # response.status_code throws an error if the form is invalid
        # Uncomment the next line if you want to return a 400 status code for invalid form
        # response.status_code = 400
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response


    def form_valid(self, form):
        """
        Handle the login form submission.

        This method checks the credentials and logs in the user if they are valid.
        """
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.login_state = True
                user.save(update_fields=['last_login', 'login_state'])
                # Optionally, you can set the user in the session
                login(self.request, user)
               
                return super().form_valid(form)
            else:
                form.add_error(None, "Invalid Password")
            
        except CustomUser.DoesNotExist:
            form.add_error(None, "User does not exist")
        return self.form_invalid(form)
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

def custom_logout_view(request):
    """
    Handle user logout.

    This view logs out the user and redirects to the index page.
    """
    if request.user.is_authenticated:
        # Change login state to False
        request.user.login_state = False
        request.user.last_login = timezone.now()  # Update last login time
        request.user.save(update_fields=['login_state','last_login'])
    # Log out the user  
        logout(request) 
         # Redirect to the index page after logout
    return redirect('login')  # Assuming 'login_view' is the name of your login URL pattern