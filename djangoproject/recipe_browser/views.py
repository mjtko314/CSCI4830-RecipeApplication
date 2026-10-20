from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'is_public', 'cuisine', 'ingredients', 'instructions']
    success_url = reverse_lazy("recipes-view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'is_public', 'cuisine', 'ingredients', 'instructions']
    success_url = reverse_lazy("recipes-view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)