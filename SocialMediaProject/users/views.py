from typing import Any
from django.contrib.auth.views import LoginView
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

from SocialMediaProject import settings
from .forms import LoginUserForm, ProfileUserForm, RegisterUserForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя',
                     'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile')

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user
