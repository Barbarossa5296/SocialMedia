from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import LoginUserForm, RegisterUserForm
from django.views.generic import CreateView


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
