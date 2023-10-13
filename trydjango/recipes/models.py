from django.db import models
from django.conf import settings
from django.urls import reverse 
# Create your models here.
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
import pint

from django.db.models import Q


class RecipeQuerySet(models.QuerySet):

    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        lookups = Q(name__icontains=query) | Q(name__icontains=query)
        return self.filter(lookups)


class RecipeManager(models.Manager):

    def get_queryset(self):
        print(f'this is db: {self.model}')
        return RecipeQuerySet(self.model, using=self.db)

    def search(self, query= None):
        return self.get_queryset().search(query=query)

class Recipe(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = RecipeManager()

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'id':self.id})
    
    def get_hx_url(self):
        return reverse('recipes:hx-detail', kwargs={'id':self.id})
    
    def get_edit_url(self):
        return reverse('recipes:edit', kwargs={'id':self.id})
    
    def get_ingredients_children(self):
        return self.recipeingredient_set.all()

class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_hx_edit_url(self):
        kwargs = {
            'parent_id': self.recipe.id,
            'id': self.id
        }
        return reverse('recipes:hx-ingredient-detail', kwargs=kwargs)


    def convert_to_system(self, system = 'mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system) 
        measurment = self.quantity_as_float * ureg[self.unit]
        print(measurment)
        return measurment #.to_base_units()

    def as_mks(self):
        measurement = self.convert_to_system(system='mks')
        print(measurement)
        return measurement.to_base_units()


    def as_imperial(self):
        measurement = self.convert_to_system(system='imperial')
        print(measurement)
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        
        print(f'cia - {self.quantity_as_float}')
        if self.quantity_as_float is not None:
            print('[ass]')
        elif qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)

# class RecipeImage():
    
#     recipe = models.ForeignKey(Recipe)
