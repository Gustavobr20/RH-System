from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Company, Department, Employee, User
from .forms import CompanyForm, DepartmentForm, EmployeeForm


def index_view(request):
    companys = Company.objects.all()
    return render(request, 'index.html', {'companys': companys})


def companyForm_view(request):
    if request.method == "GET":
        form = CompanyForm()
        return render(request, 'company_form.html', {'form': form})
    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'company_form.html', {'form': form})


def updateCompany_view(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'company_form.html', {'form': form, 'company': company})


def deleteCompany_view(request, id):
    company = Company.objects.get(id=id)

    if request.method == "GET":
        return render(request, 'delete_company.html', {'company': company})
    else:
        company.delete()
        return redirect('index')

    return render(request, 'delete_company.html')


def departmentsView(request, id):
    company = get_object_or_404(Company, id=id)
    departments = Department.objects.filter(company=company)

    return render(request, 'companys.html', {'company': company, 'departments': departments})


def departmentForm_view(request, id):
    company = get_object_or_404(Company, id=id)
    user = get_object_or_404(User)
    if request.method == "GET":
        form = DepartmentForm()
        return render(request, 'department_form.html', {'form': form, 'company': company, 'user': user})
    else:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'department_form.html', {'form': form, 'company': company, 'user': user})


def updateDepartment_view(request, id, pk):
    company = Company.objects.get(id=id)
    department = Department.objects.get(pk=pk)

    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'department_form.html', {'form': form, 'company': company, 'department': department})


def deleteDepartment_view(request, id, pk):
    company = Company.objects.get(id=id)
    department = Department.objects.get(pk=pk)

    if request.method == "GET":
        return render(request, 'delete_department.html', {'company': company, 'department': department})
    else:
        department.delete()
        return redirect('index')

    return render(request, 'delete_department.html')


def employees_view(request, id):
    company = get_object_or_404(Company, id=id)
    employees = Employee.objects.filter(company=company)

    return render(request, 'employees.html', {'company': company, 'employees': employees})


def employeeForm_view(request, id):
    company = get_object_or_404(Company, id=id)
    departments = Department.objects.filter(company=company)
    user = get_object_or_404(User)

    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'user_form.html',
                      {'form': form, 'company': company, 'user': user, 'departments': departments})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'user_form.html',
                  {'form': form, 'company': company, 'user': user, 'departments': departments})


def updateEmployee_view(request, id, pk):
    company = get_object_or_404(Company, id=id)
    departments = Department.objects.filter(company=company)
    employee = Employee.objects.get(pk=pk)

    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'user_form.html',
                  {'form': form, 'company': company, 'departments': departments, 'employee': employee})


def deleteEmployee_view(request, id, pk):
    company = get_object_or_404(Company, id=id)
    employee = Employee.objects.get(pk=pk)

    if request.method == "GET":
        return render(request, 'delete_employee.html', {'company': company, 'employee': employee})
    else:
        employee.delete()
        return redirect('index')

    return render(request, 'delete_employee.html')
