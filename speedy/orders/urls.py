from django.urls import path, include
from rest_framework import routers

from .views import OrderApiView, CreateOrderViewSet, ContactUsViewSet

router = routers.DefaultRouter()
router.register(r'create-order', CreateOrderViewSet)
router.register(r'contact-us', ContactUsViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/me/orders/', OrderApiView.as_view(), name='order_list'),
]
