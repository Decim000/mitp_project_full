from django.contrib import admin
from .models import Recipe, FullRecipe, Saved, FullRecipeSaved

# Register your models here.
admin.site.register(Recipe)
admin.site.register(FullRecipe)
admin.site.register(Saved)
admin.site.register(FullRecipeSaved)