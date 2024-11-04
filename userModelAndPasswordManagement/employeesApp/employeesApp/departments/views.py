from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from employeesApp.departments.forms import DepartmentForm, DepartmentDeleteForm
from employeesApp.departments.models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/departments-list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/department-details.html'
    context_object_name = 'department'


# @method_decorator(login_required(login_url='login'), name='dispatch') if login needed
class CreateDepartment(PermissionRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/create-department.html'
    success_url = reverse_lazy('departments list')
    permission_required = 'departments.add_department'


class EditDepartment(PermissionRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/edit-department.html'
    success_url = reverse_lazy('departments list')
    permission_required = 'departments.change_department'


class DeleteDepartment(PermissionRequiredMixin, DeleteView):
    model = Department
    form_class = DepartmentDeleteForm
    template_name = 'departments/delete-department.html'
    success_url = reverse_lazy('departments list')
    permission_required = 'departments.delete_department'

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        department = Department.objects.get(pk=pk)
        return department.__dict__
