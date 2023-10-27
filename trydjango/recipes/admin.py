from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.

from .models import Recipe, RecipeIngredient, RecipeIngredientImage



admin.site.register(RecipeIngredientImage)

class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    # fields = ['name', 'quantity', 'directions', 'unit']
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ['name', 'description', 'directions', 'timestamp', "updated" , 'active']
    sortable_by = ['user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
admin.site.register(Recipe,RecipeAdmin)




# class RecipeIngridientAdmin(admin.ModelAdmin):
#     list_display = [ 'recipe', 'name', 'description', 'directions', 'timestamp', "updated" , 'active']
#     sortable_by = ['recipe']
# admin.site.register(RecipieIngredient,RecipeIngridientAdmin)