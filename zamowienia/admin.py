from django.contrib import admin
from .models import Zamowienie, Kupon


class ZamowienieAdmin(admin.ModelAdmin):
    list_display = ('total', 'address', 'status')


class KuponAdmin(admin.ModelAdmin):
    list_display = ('code', 'percentage', 'valid_from', 'valid_to', 'active')


admin.site.register(Zamowienie, ZamowienieAdmin)
admin.site.register(Kupon, KuponAdmin)