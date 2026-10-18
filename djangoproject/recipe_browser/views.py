from django.shortcuts import render
from . import models

# Sample data (replace with database models later)
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
    }   
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'about page'})