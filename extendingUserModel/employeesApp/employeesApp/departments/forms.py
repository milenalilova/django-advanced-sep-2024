from django import forms

from employeesApp.departments.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDeleteForm(DepartmentForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
