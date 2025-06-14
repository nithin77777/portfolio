from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

from .models import User  # Assuming User model is defined in models.py
from .forms import SignupModelForm

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


def signup_view(request):
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_view')  # or wherever you want to redirect
    else:
        form = SignupModelForm()
    return render(request, 'signup_form.html', {'form': form})


class UserView(CreateView):
    """
    View for handling user-related operations.
    
    This view supports creating, listing, updating, and deleting users.
    """
    
    template_name = '../templates/signup_form.html'
    form_class = SignupModelForm
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('success_view')  # Redirect to index after successful operation

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)  # Assuming you have a function to hash passwords
        user.save()
        return super().form_valid(form)



