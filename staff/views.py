from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from staff.models import Department, Employee
from staff.forms import EmployeeForm

class DepartmentListView(ListView):
    model = Department
    template_name = 'department/deptList.html'

class DepartmenteDetailView(DetailView):

    model = Department
    template_name = 'department/deptdetail.html'

class EmployeeFormView(CreateView):
    template_name = 'employee/empForm.html'
    form_class = EmployeeForm
    success_url = '/thanks/'
