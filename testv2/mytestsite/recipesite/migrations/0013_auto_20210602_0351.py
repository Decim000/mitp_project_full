# Generated by Django 3.2.3 on 2021-06-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0012_fullrecipesaved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullrecipesaved',
            name='description1',
            field=models.TextField(verbose_name='Описание, часть 1'),
        ),
        migrations.AlterField(
            model_name='fullrecipesaved',
            name='description2',
            field=models.TextField(verbose_name='Описание, часть 2'),
        ),
        migrations.AlterField(
            model_name='fullrecipesaved',
            name='motivation',
            field=models.ImageField(upload_to='', verbose_name='Картинка мотивации'),
        ),
        migrations.AlterField(
            model_name='fullrecipesaved',
            name='preview',
            field=models.ImageField(upload_to='', verbose_name='Изображение рецепта'),
        ),
    ]