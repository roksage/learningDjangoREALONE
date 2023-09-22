from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.



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
        'object_list' : obj
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
        return redirect(obj.get_absolute_rul)
    
    return render(request, 'recipes/create-update.html', context)





@login_required
def recipe_update_view(request, id=None):

    obj = get_object_or_404(Recipe, id=id, user = request.user)

    form = RecipeForm(request.POST or None, instance=obj)


    context = {
        'form': form,
        'object_list' : obj
    }

    if form.is_valid():

        obj = form.save()

        context['massage'] = 'Data saved.'

    return render(request, 'recipes/create-update.html', context)

