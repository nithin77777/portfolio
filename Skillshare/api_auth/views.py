from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth  import login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Assuming User model is defined in models.py
from .models import User
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
    return HttpResponse("<h1>Success! User has been created/updated.</h1>")


class SignupView(CreateView):
    """
    View for handling user-related operations.

    This view supports creating, listing, updating, and deleting users.
    """

    template_name = 'signup_form.html'
    form_class = SignupModelForm
    model = User

    # Redirect to index after successful operation
    success_url = reverse_lazy('success_view')

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
    success_url = reverse_lazy('success_view')

    def form_invalid(self, form):
        """
        Handle the login form submission.

        This method checks the credentials and logs in the user if they are valid.
        """
        response = super().form_invalid(form)
        # response.status_code = 400
        return response


    def form_valid(self, form):
        """
        Handle the login form submission.

        This method checks the credentials and logs in the user if they are valid.
        """
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.login_state = True
                user.save(update_fields=['last_login', 'login_state'])
                # Optionally, you can set the user in the session
                login(self.request, user)
                # Redirect to the success URL after login
                # self.request.session['user_id'] = user.id  # Store user ID in session
                # self.request.session['username'] = user.username  # Store username in session
                # self.request.session['login_state'] = user.login_state  # Store login state in session
                return super().form_valid(form)
            else:
                form.add_error(None, "Invalid Password")
            
        except User.DoesNotExist:
            form.add_error(None, "User does not exist")
        return self.form_invalid(form)

