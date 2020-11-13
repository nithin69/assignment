from django.test import TestCase
from .models import Department, Employee

class BasicTest(TestCase):
    def test_employee(self):
        self.dept = Department.objects.create(department_name = "development")
        Employee.objects.create(employee_name = "Nithin", department = self.dept, email="nithinsaikumar69@gmail.com", date_of_birth="1993-08-24", picture="F:\projects\interviewTask\company\pictures\1.jpg")