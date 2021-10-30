from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from pr_employee.api.models import Company, Office, Department, Employee
from pr_employee.api.serializers import CompanyListSerializer, OfficeListSerializer, DepartmentSerializer, \
    EmployeeListSerializer


class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()


class OfficeListView(generics.ListCreateAPIView):
    serializer_class = OfficeListSerializer
    queryset = Office.objects.all()


class DepartmentListView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()
