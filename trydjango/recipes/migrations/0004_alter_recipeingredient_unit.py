# Generated by Django 3.2.5 on 2023-09-18 09:20

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_recipieingredient_recipeingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
