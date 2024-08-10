from django.contrib import admin
from .models import Listofproducts, ViewProduct


class ListofproductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'calories', 'fats', 'protein', 'carbohydrates')
    list_filter = ('name_product', 'calories')
admin.site.register(Listofproducts)
admin.site.register(ViewProduct)