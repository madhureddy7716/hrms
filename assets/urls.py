from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.asset_list,
        name='asset_list'
    ),

    path(
        'add/',
        views.asset_add,
        name='asset_add'
    ),
    path(
    'history/',
    views.asset_history,
    name='asset_history'
),
path(
    'history/',
    views.asset_history,
    name='asset_history'
),

    path(
        'update/<int:pk>/',
        views.asset_update,
        name='asset_update'
    ),

    path(
        'return/<int:pk>/',
        views.asset_return,
        name='asset_return'
    ),

    path(
        'delete/<int:pk>/',
        views.asset_delete,
        name='asset_delete'
    ),

]