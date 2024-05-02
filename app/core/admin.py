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
        "updated_at",
        "user_type",
        ]
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'phone_number',
            'cover_photo',
            'profile_image',
            'bio',
            'city',
            'address',
            'country',
            'state',
            'street',
            'zip_code',
            'verification_code',
            'user_type',
            )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_first_login',
                    'is_email_confirmed',
                    'is_profile_changed',
                    'is_active',
                    'is_staff',
                    'is_superuser',
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
                'birth_date',
                'gender',
                'phone_number',
                'cover_photo',
                'profile_image',
                'bio',
                'city',
                'address',
                'country',
                'state',
                'street',
                'zip_code',
                'verification_code',
                'user_type',
                'is_first_login',
                'is_email_confirmed',
                'is_profile_changed',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserType)
admin.site.register(models.Category)
admin.site.register(models.Sub_Category)
admin.site.register(models.Item)
