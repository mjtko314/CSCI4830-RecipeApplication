from django.shortcuts import render
from django.http import HttpResponse
from recipe_browser.models import Recipe
def hello(request):
    Recipe.objects.create(title="Chicken", cuisine="American", ingredients="Chicken and Salt")
    recipes = Recipe.objects.all()
    for recipe in recipes:
        title = recipe.title
    return HttpResponse(title)