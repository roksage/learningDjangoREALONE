
from django.http import HttpResponse
from articles.models import Article
from django.contrib.auth.decorators import login_required
import random

from django.template.loader import render_to_string


@login_required
def home_view(request,*args,**kwargs):
    

    article_queryset = Article.objects.all()

    context = {
        'object_list': article_queryset,

    }

   

    HTML_STRING = render_to_string('home-view.html', context = context)



    return HttpResponse(HTML_STRING)


