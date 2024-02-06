from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('api/recipe/<int:recipe_id>/', views.api_recipe_detail, name='api_recipe_detail'),
    path('api/category/<int:category_id>/', views.api_category_detail, name='api_category_detail'),
]