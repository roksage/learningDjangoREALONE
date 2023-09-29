from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    required_css_class = 'required-field'
    name = forms.CharField(help_text='This is your help')
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))



    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
        #fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for fields in self.fields:
            new_data = {
                'placeholder': f'Recipe {str(fields)}',
                'class': f'form-{str(fields)}'
            }
            self.fields[str(fields)].widget.attrs.update(new_data)

        
        self.fields['directions'].widget.attrs.update({'rows':'8'})
        self.fields['description'].widget.attrs.update({'rows':'5'})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
        #fields = '__all__'