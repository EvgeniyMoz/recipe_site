import os
import django

# Установите настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_site.settings')
django.setup()

from recipes.models import Category

def create_categories():
    # Предопределённый список осмысленных категорий
    categories_list = [
        "Напитки",
        "Основные блюда",
        "Выпечка",
        "Паста",
        "Мясные блюда",
        "Рыбные блюда",
        "Вегетарианские блюда",
        "Праздничные блюда",
        "Полезные рецепты",
        "Быстрые блюда",
        "Диетические блюда",
        "Экзотические блюда",
        "Домашние заготовки",
        "Соусы",
        "Гарниры",
    ]

    # Проверяем, существуют ли уже категории
    existing_categories = Category.objects.all()
    if existing_categories.count() >= len(categories_list):
        print("Категории уже созданы. Ничего не добавлено.")
        return

    # Создаем категории из списка
    for category_name in categories_list:
        Category.objects.get_or_create(name=category_name)
        print(f"Добавлена категория: {category_name}")

    print("Все категории успешно добавлены!")

if __name__ == "__main__":
    create_categories()