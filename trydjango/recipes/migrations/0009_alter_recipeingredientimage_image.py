# Generated by Django 3.2.5 on 2023-10-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipeingredientimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to='photos_base/'),
        ),
    ]
