from apps.hitmen.forms import UserRegisterForm, UserUpdateForm
from apps.hitmen.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    model = User
    # fields = ("email", "name", "description", "staus", "manager")
    list_display = ("email", "name", "description", "status", "manager")
    list_filter = ("email", "status")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("email", "password"),
                    "name",
                    "description",
                    "status",
                    "manager",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password", "repeat_password", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email", "name", "description")
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
