from django.views.generic import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)

class ForgotPasswordView(FormView):
    template_name = 'forgot_password_form.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            # Generate a reset token (for demo, just a random string)
            import secrets
            token = secrets.token_urlsafe(20)
            # Here, you would save the token to the user model or a separate model
            # and send an email with a reset link containing the token
            reset_link = self.request.build_absolute_uri(
                reverse_lazy('reset_password') + f'?token={token}'
            )
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                'noreply@skilldesk.com',
                [email],
                fail_silently=True,
            )
            return HttpResponse('A password reset link has been sent to your email.')
        except User.DoesNotExist:
            form.add_error('email', 'No user found with this email address.')
            return self.form_invalid(form)
