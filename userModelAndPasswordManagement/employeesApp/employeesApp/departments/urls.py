from django.urls import path, include

from employeesApp.departments import views
from employeesApp.departments.views import CreateDepartment, DeleteDepartment, EditDepartment

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='departments list'),
    path('create/', CreateDepartment.as_view(), name='create department'),
    path('<int:pk>/details/', views.DepartmentDetailView.as_view(), name='department details'),
    path('<int:pk>/delete/', DeleteDepartment.as_view(), name='delete department'),
    path('<int:pk>/edit/', EditDepartment.as_view(), name='edit department'),
]
