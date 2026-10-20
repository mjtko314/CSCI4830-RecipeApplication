from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/', views.recipes, name='recipes-view'),
    path('recipes/public/', views.public_recipes, name='public-recipes-view'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipes-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipes-delete'),
    
]