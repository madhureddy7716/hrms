from django.urls import path
from . import views

urlpatterns = [
    path(
        'apply/',
        views.apply_leave,
        name='apply_leave'
    ),
    path(
    'cancel/<int:pk>/',
    views.cancel_leave,
    name='cancel_leave'
),
]