"""
Import required libraries for admin
"""
from django.contrib import admin

from shop.models import Item, Category, Review, ProductGallery, Favorite, Purchase


class Gallery(admin.TabularInline):
    """
    Inline class for the ProductGallery model
    """
    fk_name = 'product'
    model = ProductGallery


class ItemAdmin(admin.ModelAdmin):
    """
    ModelAdmin class for the Item model
    """
    list_display = ['id', 'title', 'created_at']
    inlines = [Gallery, ]


class CategoryAdmin(admin.ModelAdmin):
    """
    ModelAdmin class for the Category model
    """
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Purchase)
