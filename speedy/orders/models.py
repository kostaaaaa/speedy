from django.db import models
from django.contrib.auth.models import User

from catalog.models import CarModel


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='orders')
    start_date = models.DateField()
    finish_date = models.DateField()
