from django.db import transaction
from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


from .models import Order
from .serializers import OrderListSerializer, CreateOrderSerializer
from catalog.models import CarModel


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user.id)
        return queryset


class CreateOrderViewSet(viewsets.ModelViewSet):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()

    @transaction.atomic
    @action(detail=False, methods=['POST'], url_path='create-order')
    def create_order(self, request):
        pk = self.request.data.get('car_id')
        car = CarModel.objects.get(pk=pk)
        start_date = self.request.data.get('start_date')
        finish_date = self.request.data.get('finish_date')
        order = Order.objects.create(user=request.user, car=car, start_date=start_date, finish_date=finish_date)
        serializer = self.get_serializer(order)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
