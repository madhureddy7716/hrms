from rest_framework.routers import DefaultRouter

from .api_views import EmployeeViewSet


router = DefaultRouter()

router.register(
    'employees',
    EmployeeViewSet
)

urlpatterns = router.urls