from django.contrib import admin    # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _


# Register your models here.
class UserAdmin(BaseUserAdmin):
    # Define the admin pages for users.

    ordering = ["id"]
    list_display = [
        "email",
        "last_name",
        "first_name",
        "created_at",
        "updated_at"
        ]
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'first_name',
            'last_name',
            'bio',
            'city',
            'address'
            )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'isEmailConfirmed',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'bio',
                'city',
                'address',
                'is_active',
                'is_staff',
                'is_superuser',
                'isEmailConfirmed',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
