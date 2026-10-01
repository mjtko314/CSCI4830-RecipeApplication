"""
URL configuration for djangoproject.

This file defines the URL routes for the Example 3 Django application.
It maps specific URL patterns to view functions inside hello_world_app.

Application Overview:
- /score/                     → Display score list and handle form submission
- /score/edit/<int:score_id>/ → Edit an existing score
- /score/delete/<int:score_id>/ → Delete an existing score

Each URL pattern connects:
    URL → View Function → Model (Score) → Template Rendering

This configuration is required for:
- Handling CRUD operations
- Supporting dynamic URL parameters (e.g., score_id)
- Enabling proper navigation within the web application
"""
from django.urls import path
from hello_world_app import views

urlpatterns = [
    path('score/', views.score_view, name='score_view'),
    path('score/edit/<int:score_id>/', views.edit_score, name='edit_score'),
    path('score/delete/<int:score_id>/', views.delete_score, name='delete_score'),
]
