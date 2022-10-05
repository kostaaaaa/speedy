from rest_framework import serializers

from .models import Order, Contact


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    car = serializers.CharField(source='car.brand.name')
    model = serializers.CharField(source='car.model')

    class Meta:
        model = Order
        fields = (
            'user',
            'car',
            'model',
            'start_date',
            'finish_date',
        )


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
