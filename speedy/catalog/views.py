from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CarModel
from .serializers import CarModelSerializer
from .utils import exclude_busy_cars


class CarModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CarModel.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        finish_date = self.request.query_params.get('finish_date', None)
        if start_date and finish_date:
            queryset = exclude_busy_cars(start_date, finish_date)
        return queryset
