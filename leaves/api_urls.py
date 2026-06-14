from rest_framework.routers import DefaultRouter

from .api_views import LeaveViewSet


router = DefaultRouter()

router.register(
    'leaves',
    LeaveViewSet
)

urlpatterns = router.urls