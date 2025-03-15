from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time')
    filter_horizontal = ('categories',)