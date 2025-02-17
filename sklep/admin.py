from django.contrib import admin
from .models import Produkt


class ProduktAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('produkt_name',)
    }
    list_display = ('produkt_name', 'price', 'stock', 'kategoria', 'is_available')

admin.site.register(Produkt, ProduktAdmin)
