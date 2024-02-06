from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Recipe

def index(request):
    # Retrieve all categories and recipes from the database
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    context = {
        'categories': categories,
        'recipes': recipes
    }
    return render(request, 'index.html', context)

def recipe_detail(request, recipe_id):
    # Retrieve the recipe with the given ID from the database
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)

def category_detail(request, category_id):
    # Retrieve the category with the given ID from the database
    category = Category.objects.get(pk=category_id)
    # Retrieve all recipes associated with the category
    recipes = category.recipe_set.all()
    context = {
        'category': category,
        'recipes': recipes
    }
    return render(request, 'category_detail.html', context)

def api_recipe_detail(request, recipe_id):
    # Retrieve the recipe with the given ID from the database
    recipe = Recipe.objects.get(pk=recipe_id)
    # Serialize the recipe data
    recipe_data = {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'categories': [category.name for category in recipe.categories.all()]
    }
    return JsonResponse(recipe_data)

def api_category_detail(request, category_id):
    # Retrieve the category with the given ID from the database
    category = Category.objects.get(pk=category_id)
    # Retrieve all recipes associated with the category
    recipes = category.recipe_set.all()
    # Serialize the category data along with associated recipes
    category_data = {
        'id': category.id,
        'name': category.name,
        'recipes': [{'id': recipe.id, 'name': recipe.name} for recipe in recipes]
    }
    return JsonResponse(category_data)