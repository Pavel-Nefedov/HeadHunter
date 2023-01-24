from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from authapp.models import HHUser


class HHUserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'patronymic',
        'is_candidate',
        'is_company',
        'is_moderator',
        'is_staff',
        'is_superuser',
        'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_company', 'is_candidate', 'is_moderator'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = [
        'last_login', 'date_joined'
    ]


admin.site.register(HHUser, HHUserAdmin)
