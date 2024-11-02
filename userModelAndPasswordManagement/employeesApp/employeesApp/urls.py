from django.contrib import admin
from django.urls import path, include

from employeesApp import employees

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employeesApp.common.urls')),
    path('departments/', include('employeesApp.departments.urls')),
    path('employees/', include('employeesApp.employees.urls')),
]
