from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    is_public = models.BooleanField(default=True)

    cuisine = models.CharField(max_length=100, default="")
    ingredients = models.TextField(blank=True, default="")
    instructions = models.TextField(blank=True, default="")

    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title