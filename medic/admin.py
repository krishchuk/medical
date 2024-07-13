from django.contrib import admin

from medic.models import Procedure


@admin.register(Procedure)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'picture',)
    search_fields = ('name', 'description',)
