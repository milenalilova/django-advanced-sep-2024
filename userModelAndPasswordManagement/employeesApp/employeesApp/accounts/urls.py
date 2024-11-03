from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from employeesApp.accounts.views import UserRegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
