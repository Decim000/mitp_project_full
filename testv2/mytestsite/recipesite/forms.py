from django import forms
from django.db import models
from django.forms import fields
from .models import FullRecipeSaved
from django.contrib.auth.forms import AuthenticationForm

class RecipeEditForm (forms.ModelForm):
    class Meta:
        model = FullRecipeSaved
        fields = ['ingredient1', 'ingredient2', 'ingredient3', 'ingredient4',
        'ingredient5', 'ingredient6', 'description1', 'description2', 'preview', 'motivation' ]


