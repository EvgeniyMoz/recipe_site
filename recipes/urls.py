from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Маршрут для деталей рецепта
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
    path('search/', views.search, name='search'),  # Маршрут для поиска
    path('add_category/', views.add_category, name='add_category'),  # Маршрут для добавления категории
]