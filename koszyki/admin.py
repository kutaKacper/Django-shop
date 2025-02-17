from django.contrib import admin
from .models import Koszyk, KoszykItem


# Register your models here.

admin.site.register(Koszyk)
admin.site.register(KoszykItem)