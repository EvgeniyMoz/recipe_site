from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Детали рецепта
    path('add/', views.add_recipe, name='add_recipe'),  # Добавление рецепта
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),  # Редактирование рецепта
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),  # Фильтрация по категориям
    path('search/', views.search, name='search'),  # Поиск рецептов
    path('add_category/', views.add_category, name='add_category'),  # Добавление категории
    path('login/', views.user_login, name='login'),  # Вход пользователя
    path('logout/', views.user_logout, name='logout'),  # Выход пользователя
    path('register/', views.register, name='register'),  # Регистрация пользователя
]