
from django.http import HttpResponse
from articles.models import Article

import random

from django.template.loader import render_to_string



def home_view(request,*args,**kwargs):
    
    random_number = random.randint(10, 100000)

    article_obj = Article.objects.get(id = random.randint(0,20))

    list_to_display = [123123,15215,15125,152512,123123,15215,15125,15251,2123123,15215,15125,152512]
    list_to_display_str = ''

    for number in list_to_display:
        list_to_display_str += f'<li> this is number {str(number)}</li>'

    article_queryset = Article.objects.all()

    context = {
        'object_list': article_queryset,
        'list_to_display_str' : list_to_display_str,
        'title' : article_obj.title,
        'id' : article_obj.id,
        'content' : article_obj.content 
    }


    HTML_STRING = render_to_string('home-view.html', context = context)

    # HTML_STRING = """
    # <h1>Hello WORLD</h1>
    # <h4>This is title:     {title}     and this is content:  {content}  and this is id: {id} </h4>

    # """.format(**context)


    return HttpResponse(HTML_STRING)