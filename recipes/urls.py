from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('register/', views.register, name='register'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
]