from django.urls import path

from study.views import (DepartmentAPIView, EmployeeAPIView, ProjectAPIView,
                         DepartmentListAPIView, EmployeeListAPIView, ProjectListAPIView)

urlpatterns= [
    path('departments/', DepartmentAPIView.as_view(), name='department'),
    path('employees/', EmployeeAPIView.as_view(), name='employee'),
    path('projects/', ProjectAPIView.as_view(), name='project'),
    path('departments/<int:department_id>', DepartmentListAPIView.as_view(), name='department-detail'),
    path('employees/<int:employee_id>', EmployeeListAPIView.as_view(), name='employee-detail'),
    path('projects/<int:project_id>', ProjectListAPIView.as_view(), name='project-detail'),

]