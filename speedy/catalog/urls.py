from rest_framework import routers

from .views import CarModelViewSet

router = routers.DefaultRouter()
router.register('', CarModelViewSet, basename='cars')

urlpatterns = router.urls
