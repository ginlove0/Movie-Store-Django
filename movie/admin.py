from django.contrib import admin
from .models import Movie, Type
# Register your models here.

class TypeAdmin(admin.TabularInline):
    model = Type

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', 'datetime_release','get_type')
    list_filter = ('name', 'datetime_release', 'type')

    def get_type(self, obj):
        return ",\n".join([t.name for t in obj.type.all()])


admin.site.register(Movie, MovieAdmin)
admin.site.register(Type)