from rest_framework import routers

from .views import CarModelViewSet

router = routers.DefaultRouter()
router.register('v1/catalog', CarModelViewSet, basename='cars')

urlpatterns = router.urls
