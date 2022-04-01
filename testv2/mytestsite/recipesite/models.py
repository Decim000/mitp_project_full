from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe (models.Model):
    title = models.CharField('Название', max_length=40)
    description = models.TextField('Описание')
    photo = models.ImageField()
    #link = models.TextField('Ссылка')
    save_check = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Saved (models.Model):
    
    title = models.CharField('Название', max_length=40)
    description = models.TextField('Описание')
    photo = models.ImageField()
    link = models.TextField('Ссылка')
    owner = models.CharField('Владелец', blank=True, null=True, max_length=20 )
    

    def __str__(self):
        return self.title


class FullRecipe (models.Model):
    title = models.CharField('Название', max_length=40)
    ingredient1 = models.CharField('Ингредиент 1', max_length=30, null=True, blank=True)
    ingredient2 = models.CharField('Ингредиент 2', max_length=30, null=True, blank=True)
    ingredient3 = models.CharField('Ингредиент 3', max_length=30, null=True, blank=True)
    ingredient4 = models.CharField('Ингредиент 4', max_length=30, null=True, blank=True)
    ingredient5 = models.CharField('Ингредиент 5', max_length=30, null=True, blank=True)
    ingredient6 = models.CharField('Ингредиент 6', max_length=30, null=True, blank=True)
    description1 = models.TextField('Описание1')
    description2 = models.TextField('Описание2')
    preview = models.ImageField()
    motivation = models.ImageField()
    preview_image = models.CharField('К кому относится', max_length=40, null=True)


    def __str__(self):
        return self.title


class FullRecipeSaved (models.Model):
    title = models.CharField('Название', max_length=40)
    ingredient1 = models.CharField('Ингредиент 1', max_length=30, null=True, blank=True)
    ingredient2 = models.CharField('Ингредиент 2', max_length=30, null=True, blank=True)
    ingredient3 = models.CharField('Ингредиент 3', max_length=30, null=True, blank=True)
    ingredient4 = models.CharField('Ингредиент 4', max_length=30, null=True, blank=True)
    ingredient5 = models.CharField('Ингредиент 5', max_length=30, null=True, blank=True)
    ingredient6 = models.CharField('Ингредиент 6', max_length=30, null=True, blank=True)
    description1 = models.TextField('Описание, часть 1')
    description2 = models.TextField('Описание, часть 2')
    preview = models.ImageField('Изображение рецепта')
    motivation = models.ImageField('Картинка мотивации')
    preview_image = models.CharField('К кому относится', max_length=40, null=True)


    def __str__(self):
        return self.title