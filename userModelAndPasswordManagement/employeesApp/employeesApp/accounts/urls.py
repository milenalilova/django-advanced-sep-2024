from django.urls import path

from employeesApp.accounts import views

urlpatterns = [
    path('', views.UserRegisterView.as_view(), name='register'),
]
