from django.contrib import admin

from .models import Order, Contact


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car',
        'start_date',
        'finish_date',
    )
    search_fields = ('user__username', 'car_id__brand_id__name', 'car_id__model',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'message',
        'created_at',
    )
    search_fields = ('email', 'phone')


admin.site.register(Contact, ContactUsAdmin)
admin.site.register(Order, OrderAdmin)
