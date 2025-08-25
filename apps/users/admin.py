from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Admin panelinde görünen alanlar
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    # Mevcut kullanıcıyı düzenlerken gözüken alanlar
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Kişisel Bilgiler", {"fields": ("first_name", "last_name", "phone")}),
        ("Yetkiler", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Önemli Tarihler", {"fields": ("last_login", "date_joined")}),
    )

    # Yeni kullanıcı eklerken gözüken alanlar
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2")}  # sadece email ve şifre
        ),
    )
