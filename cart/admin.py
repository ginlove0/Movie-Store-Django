from django.contrib import admin

# Register your models here.

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','quantity','movies')
    def has_add_permission(self, request, obj=None):
        return False
    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Cart,CartAdmin)