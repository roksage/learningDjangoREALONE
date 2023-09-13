from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404


@login_required
def article_detail_view(request, slug = None):
    article_obj = None

    if slug is not None:
        try:
            article_obj = Article.objects.get(slug = slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
        
    context = {
        'object' : article_obj,
    }
    print(context)
    return render(request, "articles/detail.html", context=context) 


@login_required
def article_create_view(request):

    form = ArticleForm(request.POST or None)
    
    context = {
        'form': form
    }
    print(context)
    if form.is_valid():
        article_object = form.save()

        article_id = Article.objects.get(id = article_object.id)

        context['form'] = ArticleForm(instance=article_object)

        context['created'] = True
        context['slug'] = article_id.slug
        print(context['slug'])
    return render(request, "articles/create.html", context=context) 




@login_required
def article_search_view(request):

    query = request.GET.get('query')
    qs = Article.objects.search(query=query)
    context = {
        "object_list": qs
    }
    print(context['object_list'])

    
    return render(request, "articles/search.html", context=context)



