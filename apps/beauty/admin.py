from django.contrib import admin
from .models import Category, Product, Wishlist, Rating, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
    search_fields = ("user__username", "product__name")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "score", "created_at")
    list_filter = ("score", "created_at")
    search_fields = ("user__username", "product__name")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "text", "created_at")
    search_fields = ("user__username", "product__name", "text")
