from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.JSONField()  # Using JSONField for ingredients
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name