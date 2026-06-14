from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path(
    'hr/dashboard/',
    views.hr_dashboard,
    name='hr_dashboard'
),

    path('employees/', views.employee_list, name='employee_list'),

    path('add/', views.employee_add, name='employee_add'),

    path(
        'update/<int:pk>/',
        views.employee_update,
        name='employee_update'
    ),

    path(
        'delete/<int:pk>/',
        views.employee_delete,
        name='employee_delete'
    ),

    path('profile/', views.profile, name='profile'),

    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),

    path(
        'leave/',
        views.apply_leave,
        name='apply_leave'
    ),

    path(
        'leave-history/',
        views.leave_history,
        name='leave_history'
    ),

    path(
        'change-password/',
        views.change_password,
        name='change_password'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    
]