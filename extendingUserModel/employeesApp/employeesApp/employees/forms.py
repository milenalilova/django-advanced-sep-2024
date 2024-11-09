from django import forms

from employeesApp.employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        error_messages = {
            'first_name': {
                'required': 'Please enter your first name.',
                'max_length': 'First name cannot exceed 100 characters.',
            },
        }


class EmployeeDeleteForm(EmployeeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class EmployeeSearchForm(forms.Form):
    # TODO fix the SearchForm
    query = forms.CharField(
        label='Search Employees',
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search Employees'}
        )
    )


class EmployeeFeedbackForm(forms.Form):
    author_name = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
