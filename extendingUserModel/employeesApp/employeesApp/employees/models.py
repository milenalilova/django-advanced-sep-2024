from django.db import models

from employeesApp.departments.models import Department


class Employee(models.Model):
    class PositionChoices(models.TextChoices):
        STAFF = 'Staff', 'Staff'
        MANAGER = 'Manager', 'Manager'

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=PositionChoices.choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
