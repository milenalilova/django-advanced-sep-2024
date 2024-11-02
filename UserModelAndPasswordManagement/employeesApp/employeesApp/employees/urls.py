from django.urls import path
from employeesApp.employees import views
from employeesApp.employees.views import CreateEmployee, EmployeeDetails, EmployeesList

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees list'),
    path('create/', CreateEmployee.as_view(), name='create employee'),
    path('details/<int:pk>/', EmployeeDetails.as_view(), name='employee details'),
    path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete employee'),
]
