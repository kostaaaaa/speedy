from rest_framework import generics, viewsets, response, status, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Order, Contact
from .serializers import OrderListSerializer, CreateOrderSerializer, ContactUsSerializer
from catalog.models import CarModel


class OrderApiView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user.id)
        return queryset


class CreateOrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request):
        pk = self.request.data.get('car_id')
        car = CarModel.objects.get(pk=pk)
        start_date = self.request.data.get('start_date')
        finish_date = self.request.data.get('finish_date')
        order = Order.objects.create(user=request.user, car=car, start_date=start_date, finish_date=finish_date)
        serializer = self.get_serializer(order)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactUsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ContactUsSerializer
    queryset = Contact.objects.all()
    permission_classes = [AllowAny]
