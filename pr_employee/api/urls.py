from django.urls import path

from pr_employee.api import views

urlpatterns = [

    path('company/list/', views.CompanyListView.as_view()),
    path('office/list/', views.OfficeListView.as_view()),
    path('department/list', views.DepartmentListView.as_view()),
    path('employee/list', views.EmployeeListView.as_view())
]
