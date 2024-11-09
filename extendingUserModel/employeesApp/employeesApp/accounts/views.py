from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from employeesApp.accounts.forms import CustomUserForm


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):
    pass
# Could extend the Logout view to a custom
