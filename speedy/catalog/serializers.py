from rest_framework import serializers

from .models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    engine_capacity = serializers.CharField(source='engine.capacity')
    power = serializers.CharField(source='engine.power')
    engine_type = serializers.CharField(source='engine.type')

    class Meta:
        model = CarModel
        fields = (
            'brand_name',
            'model',
            'engine_capacity',
            'engine_type',
            'power',
            'body_type',
            'year',
            'image',
        )
