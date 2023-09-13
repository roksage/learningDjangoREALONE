"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import (article_search_view, article_create_view, article_detail_view)

from accounts.views import (login_view,register_view,logout_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('articles/', article_search_view, name = 'article-search'),
    path('articles/create', article_create_view, name='article-create'),
    path('articles/<slug:slug>/', article_detail_view, name='article-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name='logout'),

]
