from django.shortcuts import render
from articles.models import Article
# Create your views here.
from recipes.models import Recipe



SEARCH_TYPE_MAPPING = {
    'article': Article,
    'articles': Article,
    'recipe': Recipe,
    'recipes': Recipe,   
}

def search_view(request):

    query = request.GET.get('query')
    search_type = request.GET['type']


    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]

    print(Klass)

    qs = Klass.objects.search(query=query)

    print(qs)

    context = {
        "queryset": qs
    }

    template = 'search/results_view.html'
    if request.htmx:
        context = {"queryset": qs[:5]}

        template = 'search/partials/results.html'
    return render(request, template, context)