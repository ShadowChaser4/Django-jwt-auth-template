from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = User
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password","first_name","middle_name","last_name", )}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2","role","first_name","last_name","middle_name", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    list_display = ('email', 'first_name', 'middle_name', 'last_name', )
    search_fields = ("email","first_name","last_name")
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)