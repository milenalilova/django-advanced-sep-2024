from django.urls import reverse_lazy
from django.views.generic import CreateView

from employeesApp.accounts.forms import CustomUserForm


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')
