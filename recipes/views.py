from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Recipe, Category
from .forms import RecipeForm, RegisterForm
from django.core.paginator import Paginator

# Главная страница
def home(request):
    recipes = Recipe.objects.all().order_by('?')
    paginator = Paginator(recipes, 6)  # 6 рецептов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'recipes/home.html', {'page_obj': page_obj, 'categories': categories})

# Страница деталей рецепта
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Добавление рецепта
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()  # Сохраняем связанные категории
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'recipes/register.html', {'form': form})

# Фильтрация рецептов по категориям
def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(categories=category)
    return render(request, 'recipes/category_recipes.html', {'category': category, 'recipes': recipes})

# Редактирование рецепта
@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/add_recipe.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
    return redirect('home')

def search(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(title__icontains=query) if query else []
    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query})