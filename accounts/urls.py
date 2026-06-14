from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.select_profile,
        name='home'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'hr-login/',
        views.hr_login,
        name='hr_login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]