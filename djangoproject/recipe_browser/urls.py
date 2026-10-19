from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes', views.recipes, name='recipes-view'),
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes-detail'),
    
]