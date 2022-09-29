from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car',
        'start_date',
        'finish_date',
    )
    search_fields = ('user__username', 'car_id__brand_id__name', 'car_id__model',)


admin.site.register(Order, OrderAdmin)
