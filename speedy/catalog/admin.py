from django.contrib import admin

from .models import Brand, CarModel, Engine


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity', 'power',)


class EngineInLine(admin.TabularInline):
    model = Engine


class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'engine',
        'body_type',
        'year',
        'is_available',
    )
    search_fields = ('brand__name', 'model', 'year',)
    list_filter = (
        'body_type',
        'is_available',
    )


admin.site.register(Brand, BrandAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(CarModel, CarModelAdmin)
