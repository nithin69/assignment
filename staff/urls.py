from django.urls import path
from staff.views import DepartmentListView, DepartmenteDetailView, EmployeeFormView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('department/<int:pk>/', DepartmenteDetailView.as_view(), name='detail-department'),
    path('empform/', EmployeeFormView.as_view(), name='create-employee'),
]