# Generated by Django 3.2.3 on 2021-05-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0002_fullrecipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.TextField(default='', verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]