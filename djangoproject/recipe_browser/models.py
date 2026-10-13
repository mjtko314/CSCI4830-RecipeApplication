from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    cuisine = models.CharField(max_length=100)
    ingredients = models.TextField(blank=True, default="")
    instructions = models.TextField(blank=True, default="")
    #date_added = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.title