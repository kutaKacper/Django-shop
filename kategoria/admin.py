from django.contrib import admin
from .models import Kategoria


class KategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('kategoria_name',)
    }
    list_display = ('kategoria_name', 'slug')

admin.site.register(Kategoria, KategoriaAdmin)
