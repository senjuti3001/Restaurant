from django.contrib import admin

# import from model
from restuarant.model.models import Category, Menu


# Register your models here.
# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'name', 'price', 'quantity']
