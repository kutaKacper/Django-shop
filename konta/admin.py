from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Konto


class KontoAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'username', 'email', 'date_joined', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    list_display_links = ('first_name', 'last_name', 'phone', 'email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)


admin.site.register(Konto, KontoAdmin)
