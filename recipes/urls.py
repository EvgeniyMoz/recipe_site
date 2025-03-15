from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),  # Маршрут для добавления рецепта
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),  # Маршрут для редактирования рецепта
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
    path('add_category/', views.add_category, name='add_category'),
    path('search/', views.search, name='search'),
]