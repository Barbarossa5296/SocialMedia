from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import LoginUserForm

# def login_user(request):
#     return HttpResponse("login")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


# def logout_user(request):
#     return HttpResponse("logout")
