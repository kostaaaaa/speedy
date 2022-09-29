from django.urls import include, path
from rest_framework import routers

from .views import OrderViewSet, CreateOrderViewSet

router = routers.DefaultRouter()
router.register('me/orders', OrderViewSet, basename='orders')
router.register('orders', CreateOrderViewSet, basename='create_order')

urlpatterns = [
    path('', include(router.urls)),
]
