from django.contrib import admin
from .models import Department, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'department', 'email', 'date_of_birth', 'picture')
    list_filter = ('department__department_name', 'date_of_birth')

class EmployeeInlinAdmin(admin.TabularInline):
    model = Employee

class DepartmentAdmin(admin.ModelAdmin):
   inlines = [EmployeeInlinAdmin,]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
