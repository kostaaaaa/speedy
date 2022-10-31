from django.db.models import Q

from orders.models import Order
from .models import CarModel


def exclude_busy_cars(start_date, finish_date):
    dates_filter = Order.objects.all().filter(
        Q(start_date__range=(start_date, finish_date)) |
        Q(finish_date__range=(start_date, finish_date))
        )
    temp = set(list(dates_filter.values_list('car')))
    busy_car_id_list = [el[0] for el in temp]
    queryset = CarModel.objects.exclude(pk__in=busy_car_id_list)
    return queryset
