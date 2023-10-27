# Generated by Django 3.2.5 on 2023-10-24 11:33

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipeingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.FileField(upload_to='photos_base/', validators=[recipes.validators.validate_zip_extension]),
        ),
    ]