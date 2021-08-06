from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('company/add', views.companyForm_view, name='companys'),
    path('update/<int:id>', views.updateCompany_view, name='update_company'),
    path('delete/<int:id>', views.deleteCompany_view, name='delete_company'),
    path('<int:id>/departments', views.departmentsView, name='departments'),
    path('<int:id>/departments/add', views.departmentForm_view, name='create_department'),
    path('<int:id>/update/<int:pk>/', views.updateDepartment_view, name='update_department'),
    path('<int:id>/delete/<int:pk>/', views.deleteDepartment_view, name='delete_department'),
    path('<int:id>/employees', views.employees_view, name='employees'),
    path('<int:id>/employees/add', views.employeeForm_view, name='create_employee'),
    path('<int:id>/update-employee/<int:pk>', views.updateEmployee_view, name='update_employee'),
    path('<int:id>/delete-employee/<int:pk>', views.deleteEmployee_view, name='delete_employee'),
]
