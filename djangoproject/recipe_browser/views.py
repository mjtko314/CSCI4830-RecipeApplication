from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


def home(request):
    recipes = models.Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'about page'})


def recipes(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': all_recipes})


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipe_browser/home.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipe_detail.html'