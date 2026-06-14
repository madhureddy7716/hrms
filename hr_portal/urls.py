from django.urls import path
from . import views

urlpatterns = [


path(
    'dashboard/',
    views.hr_dashboard,
    name='hr_dashboard'
),

path(
    'employees/',
    views.employee_list,
    name='employee_list'
),

path(
    'leaves/',
    views.leave_requests,
    name='leave_requests'
),

path(
    'approve/<int:pk>/',
    views.approve_leave,
    name='approve_leave'
),

path(
    'reject/<int:pk>/',
    views.reject_leave,
    name='reject_leave'
),

path(
    'disable/<int:pk>/',
    views.disable_employee,
    name='disable_employee'
),


]
