from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField('Nome Fantasia', max_length=255, unique=True,)
    legal_number = models.CharField('CNPJ', max_length=14, unique=True, default="")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField('Departamento', max_length=255)
    status = models.BooleanField(default=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    gender = models.CharField(max_length=1, choices=GENDER)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    role = models.CharField(max_length=50, default='Sem Atribuição')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return str(self.name)
