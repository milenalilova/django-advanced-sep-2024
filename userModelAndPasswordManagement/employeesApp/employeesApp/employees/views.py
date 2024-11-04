from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from employeesApp.employees.forms import EmployeeForm, EmployeeDeleteForm, EmployeeSearchForm, EmployeeFeedbackForm
from employeesApp.employees.models import Employee


class EmployeesList(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employees/employees-list.html'
    paginate_by = 3

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetails(DetailView):
    model = Employee
    template_name = 'employees/employee-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = EmployeeFeedbackForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = EmployeeFeedbackForm(request.POST)

        print("Post method called")
        print("Form data:", request.POST)

        if form.is_valid():
            print("Form is valid.")
            print("Cleaned data:", form.cleaned_data)
            messages.success(request, 'Thank you for your feedback!')
            # return self.get(request, *args, **kwargs)  # Redirect back to the detail view
            return redirect('employees list')


        else:
            print("Form is invalid.")
            print("Errors:", form.errors)
            messages.error(request, 'There were errors in your submission. Please correct them.')
            context = self.get_context_data(feedback_form=form)  # Pass the form with errors
            return self.render_to_response(context)


class CreateEmployee(PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = Employee
    template_name = 'employees/create-employee.html'
    success_url = reverse_lazy('employees list')


class DeleteEmployee(PermissionRequiredMixin,DeleteView):
    model = Employee
    form_class = EmployeeDeleteForm
    template_name = 'employees/delete-employee.html'
    success_url = reverse_lazy('employees list')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        employee = Employee.objects.get(pk=pk)
        return employee.__dict__
