from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class LogInView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/login.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


