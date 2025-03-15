from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from django.core.paginator import Paginator

def home(request):
    recipes = Recipe.objects.all().order_by('?')
    paginator = Paginator(recipes, 6)  # 6 рецептов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'recipes/home.html', {'page_obj': page_obj, 'categories': categories})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

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

def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(categories=category)
    return render(request, 'recipes/category_recipes.html', {'category': category, 'recipes': recipes})