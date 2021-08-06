from django import forms
from .models import Company, Department, Employee


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'legal_number')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legal_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('company', 'name', 'status', 'Admin')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'age', 'gender', 'company', 'department', 'user', 'phone', 'role', 'salary', 'joining_date')
