from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


# Admin

path(
    'admin/',
    admin.site.urls
),

# API URLs

path(
    'api/',
    include('employees.api_urls')
),

path(
    'api/',
    include('leaves.api_urls')
),

path(
    'api/',
    include('assets.api_urls')
),

path(
    'api/',
    include('accounts.api_urls')
),

# Employee Portal

path(
    '',
    include('accounts.urls')
),

path(
    '',
    include('employees.urls')
),

# Leave Module

path(
    'leave/',
    include('leaves.urls')
),

# Asset Module

path(
    'assets/',
    include('assets.urls')
),

# HR Portal

path(
    'hr/',
    include('hr_portal.urls')
),


]

if settings.DEBUG:


 urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

