from django.contrib import admin
from .models import Artwork, Category

# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Artwork, ProductAdmin)
admin.site.register(Category, CategoryAdmin)