import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Category, Recipe

def populate_data():
    # Creating sample categories
    categories = ['Breakfast', 'Lunch', 'Dinner']
    for category_name in categories:
        category, created = Category.objects.get_or_create(name=category_name)
        if created:
            print(f'Created category: {category}')

    # Creating sample recipes
    recipes = [
        {"name": "Scrambled Eggs", "ingredients": ["eggs", "salt", "pepper"], "categories": ["Breakfast"]},
        {"name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "bacon", "parmesan"], "categories": ["Lunch", "Dinner"]},
        {"name": "Chicken Stir-Fry", "ingredients": ["chicken", "vegetables", "soy sauce"], "categories": ["Lunch", "Dinner"]},
        {"name": "Pancakes", "ingredients": ["flour", "milk", "eggs", "butter"], "categories": ["Breakfast"]},
        {"name": "Grilled Salmon", "ingredients": ["salmon", "lemon", "olive oil"], "categories": ["Dinner"]}
    ]

    for recipe_data in recipes:
        recipe = Recipe.objects.create(
            name=recipe_data['name'],
            ingredients=recipe_data['ingredients']
        )
        for category_name in recipe_data['categories']:
            category = Category.objects.get(name=category_name)
            recipe.categories.add(category)
        print(f'Created recipe: {recipe}')

if __name__ == '__main__':
    populate_data()