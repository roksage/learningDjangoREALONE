from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.forms.models import modelformset_factory
from .models import RecipeIngredient

@login_required
def recipe_list_view(request, id=None):

    qs = Recipe.objects.filter(user=request.user)

    context = {
        'object_list' : qs
    }

    return render(request, 'recipes/list.html', context)





@login_required
def recipe_detail_view(request, id=None):

    obj = get_object_or_404(Recipe, id=id, user = request.user)

    context = {
        'object' : obj
    }

    return render(request, 'recipes/detail.html', context)






@login_required
def recipe_create_view(request, id=None):

    form = RecipeForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    
    return render(request, 'recipes/create-update.html', context)





@login_required
def recipe_update_view(request, id=None):

    obj = get_object_or_404(Recipe, id=id, user = request.user)

    form = RecipeForm(request.POST or None, instance=obj)

    # Formset = modelform_factory(Model, form=ModelForm, extra=0 )

    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, RecipeIngredientForm, extra = 1)
    qs = obj.get_ingredients_children()
    formset=RecipeIngredientFormset(request.POST or None, queryset=qs)

    context = {
        'form': form,
        'object': obj,
        'formset': formset,
    }


    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()

        for form in formset:
            child = form.save(commit = False)
            child.recipe = parent
            child.save()

        context['message'] = 'Data saved.'

    return render(request, 'recipes/create-update.html', context)

