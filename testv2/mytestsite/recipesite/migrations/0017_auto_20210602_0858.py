# Generated by Django 3.2.3 on 2021-06-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0016_auto_20210602_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullrecipesaved',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient1',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 1'),
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient2',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 2'),
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient3',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 3'),
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient4',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 4'),
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient5',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 5'),
        ),
        migrations.AddField(
            model_name='fullrecipesaved',
            name='ingredient6',
            field=models.CharField(max_length=30, null=True, verbose_name='Ингредиент 6'),
        ),
    ]
