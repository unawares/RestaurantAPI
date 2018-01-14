from django.contrib import admin
from .models import Category, Food, FoodImage

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug']
   prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class FoodAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
   list_filter = ['available', 'created', 'updated']
   list_editable = ['price', 'available']
   prepopulated_fields = {'slug': ('name',)}

admin.site.register(Food, FoodAdmin)


class FoodImageAdmin(admin.ModelAdmin):
   list_display = ['name']

admin.site.register(FoodImage, FoodImageAdmin)
