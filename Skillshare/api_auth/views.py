from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.utils import timezone
from .models import CustomUser
from .forms import SignupModelForm, LoginForm


def index(request):
    """
    Render the index page with error handling.
    """
    try:
        return HttpResponse("""<h1>Hello, world! This is the index page. </h1>""")
    except Exception:
        return HttpResponse("<h1>Something went wrong. Please try again later.</h1>", status=500)


def success_view(request):
    """
    Render the success page after a successful operation with error handling.
    """
    try:
        return HttpResponse("<h1>Success! User has been created/updated.</h1>")
    except Exception:
        return HttpResponse("<h1>Something went wrong. Please try again later.</h1>", status=500)


class SignupView(CreateView):
    template_name = 'signup_form.html'
    form_class = SignupModelForm
    model = CustomUser
    success_url = reverse_lazy('success_view')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login_form.html'
    success_url = reverse_lazy('success_view')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.login_state = True
                user.save(update_fields=['last_login', 'login_state'])
                login(self.request, user)
                user.login_state = True
                user.save(update_fields=['login_state'])
                return super().form_valid(form)
            else:
                form.add_error(None, "Invalid Password")
        except CustomUser.DoesNotExist:
            form.add_error(None, "User does not exist")
            return self.form_invalid(form)

def custom_logout_view(request):
    """
    Handle user logout with error handling.
    """
    try:
        if request.user.is_authenticated:
            request.user.login_state = False
            request.user.last_login = timezone.now()
            request.user.save(update_fields=['login_state','last_login'])
            logout(request)
        return HttpResponse('<h1>You Have Been Logged Out</h1>')
    except Exception:
        return HttpResponse("<h1>Something went wrong during logout. Please try again later.</h1>", status=500)