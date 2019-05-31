
from django.contrib import admin
from .models import Order, Shipment, MovieStatus, MovieOrder
# Register your models here.

class OrderAdmin(admin.TabularInline):
    model = MovieOrder


class MovieOrderAdmin(admin.ModelAdmin):
    list_display = ('status','shipment', 'customer')
    inlines = [
        OrderAdmin,
    ]


admin.site.register(Order, MovieOrderAdmin)
admin.site.register(Shipment)
admin.site.register(MovieStatus)
admin.site.register(MovieOrder)