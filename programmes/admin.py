from django.contrib import admin
from .models import Programme, Category

# Register your models here.

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly-name',
        'name',
    )


admin.site.register(Programme)
admin.site.register(Category)
