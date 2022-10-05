from django.db import models
from django.contrib.auth.models import User

from catalog.models import CarModel


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='orders')
    start_date = models.DateField()
    finish_date = models.DateField()


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=12)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
