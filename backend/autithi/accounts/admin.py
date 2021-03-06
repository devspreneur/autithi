from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Address
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'email',
        'username',
        'address',
        'full_name',
        'date_of_birth',
        'is_admin',
        'is_verified',
        'profile_image',
    )
    list_filter = ('is_admin',)
    fieldsets = (
        (
            None,
            {
                'fields': ('email', 'username', 'address', 'full_name', 'password')
            }
        ),
        (
            'Personal info',
            {
                'fields': ('date_of_birth','profile_image')
            }
        ),
        (
            'Permissions',
            {
                'fields': ('is_staff', 'is_admin', 'is_verified')
            }
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'full_name',
                    'email',
                    'date_of_birth',
                    'password1',
                    'password2',
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Address)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
