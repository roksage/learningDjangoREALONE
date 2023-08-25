
from django.http import HttpResponse
from articles.models import Article

import random

from django.template.loader import render_to_string



def home_view(request,*args,**kwargs):
    

    article_queryset = Article.objects.all()

    context = {
        'object_list': article_queryset,

    }


    HTML_STRING = render_to_string('home-view.html', context = context)

    # HTML_STRING = """
    # <h1>Hello WORLD</h1>
    # <h4>This is title:     {title}     and this is content:  {content}  and this is id: {id} </h4>

    # """.format(**context)


    return HttpResponse(HTML_STRING)


