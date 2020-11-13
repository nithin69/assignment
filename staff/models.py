from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100, verbose_name='Employee_name', null=False, blank=False)
    department = models.ForeignKey('Department', related_name="department", on_delete=models.CASCADE)
    email = models.EmailField(max_length = 150, verbose_name ='Email', null= True, blank= True)
    date_of_birth = models.DateField(verbose_name ='Date Of Birth', null= True, blank= True)
    picture = models.ImageField(upload_to ='pictures/', null= True, blank= True)
    def __str__(self):
        return self.employee_name

class Department(models.Model):
    department_name = models.CharField(max_length=100, verbose_name = 'Department Name', null=False, blank=False)
    manager = models.ForeignKey(Employee, related_name="employee", on_delete=models.CASCADE, null=True, blank = True)
    def __str__(self):
        return self.department_name
