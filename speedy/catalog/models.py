from django.db import models

ENGINE_TYPE_CHOICES = [
    ('Benzin', 'Benzin'), ('Diesel', 'Diesel'),
    ('Hybrid', 'Hybrid'), ('Electric', 'Electric'),
]
BODY_TYPE_CHOICES = [
    ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'),
    ('Touring', 'Touring'), ('Coupe', 'Coupe'),
    ('Minivan', 'Minivan'), ('Bus', 'Bus'),
]


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=ENGINE_TYPE_CHOICES, default='Benzin')
    capacity = models.FloatField(blank=True, null=True)
    power = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    model = models.CharField(max_length=50)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='engine')
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, default='Sedan')
    year = models.PositiveIntegerField(default=1900)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'
