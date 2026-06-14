from rest_framework.routers import DefaultRouter

from .api_views import AssetViewSet


router = DefaultRouter()

router.register(
    'assets',
    AssetViewSet
)

urlpatterns = router.urls