from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from . import models


def home(request):
    return render(request, 'home.html')

def search_recipes(queryset, query):
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
            | Q(cuisine__icontains=query)
            | Q(ingredients__icontains=query)
        )
    return queryset

@login_required
def recipes(request):
    query = request.GET.get("q", "").strip()
    user_recipes = models.Recipe.objects.filter(author=request.user)
    user_recipes = search_recipes(user_recipes, query)
    return render(request, 'recipes.html', {
        'recipes': user_recipes,
        'page_title': 'My Recipes',
        'query': query,
    })

def public_recipes(request):
    query = request.GET.get("q", "").strip()
    pub = models.Recipe.objects.filter(is_public=True)
    pub = search_recipes(pub, query)
    return render(request, 'public_recipes.html', {
        'recipes': pub,
        'page_title': 'Public Recipes',
        'query': query,
    })

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

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'is_public', 'cuisine', 'ingredients', 'instructions']
    success_url = reverse_lazy("recipes-view")

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy("recipes-view")

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author