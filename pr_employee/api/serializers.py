from rest_framework import serializers

from pr_employee.api.models import Company, Department, Office, Employee


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'created_date', 'name', 'ceo', 'phone', 'logo']


class OfficeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'name', 'region', 'location', 'phone']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'd_name', 'location']


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'gender', 'phone', 'picture', 'department', 'office', 'office', 'companies']
