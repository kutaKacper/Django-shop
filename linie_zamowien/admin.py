from django.contrib import admin
from .models import LiniaZamowienia


class LiniaZamowieniaAdmin(admin.ModelAdmin):
    list_display = ('produkt', 'quantity', 'price')

admin.site.register(LiniaZamowienia, LiniaZamowieniaAdmin)
