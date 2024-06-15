from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'age', 'is_staff', 'is_active')

    field_sets = UserAdmin.fieldsets + ((None, {'fields': ('age', )}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', )}), )


admin.site.register(CustomUser, CustomUserAdmin)
