from django.contrib import admin

# Register your models here.
from pr_employee.api.models import Company, Office, Department, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ceo', 'phone', 'company_slogan', 'logo']
    search_fields = ['name', 'ceo', 'phone']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'company', 'name', 'region', 'location', 'phone']

    date_hierarchy = 'created_date'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'd_name', 'location']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'gender', 'phone', 'picture', 'department', 'office', 'office', 'companies']
