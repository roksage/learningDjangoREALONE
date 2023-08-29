from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib.auth import authenticate, login, logout


@login_required
def article_detail_view(request, id = None):
    article_obj = None

    if id is not None:
        article_obj = Article.objects.get(id = id)

    context = {
        'object' : article_obj,
    }


    return render(request, "articles/search.html", context=context) 


@login_required
def article_create_view(request):

    form = ArticleForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        
        context['created'] = True

    return render(request, "articles/create.html", context=context) 




# @login_required
# def article_create_view(request):

#     form = ArticleForm()

#     context = {
#         'form': form
#     }


#     if request.method == "POST":

#         form = ArticleForm(request.POST)
#         context['form'] = form
#         print(context)
#         if form.is_valid():
#             title_of_post = form.cleaned_data.get('title')
#             content_of_post = form.cleaned_data.get('content')
#             article_object = Article.objects.create(title = title_of_post, content = content_of_post)

#             context['object'] = article_object
#             context['created'] = True
#             print(context)
#     return render(request, "articles/create.html", context=context) 


@login_required
def article_search_view(request):

    article_obj = None



    query_dict = request.GET



    try:
        query = int(query_dict.get('query'))
    except:
        query = None

    

    if query is not None:
        article_obj = Article.objects.get(id = query)


    context = {
        'object' : article_obj,
    }

    print(context)

    return render(request, 'articles/search.html', context=context)



