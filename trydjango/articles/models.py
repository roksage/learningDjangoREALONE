from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title 
from django.urls import reverse
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):

    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):

    def get_queryset(self):
        print(f'this is db: {self.model}')
        return ArticleQuerySet(self.model, using=self.db)


    def search(self, query= None):
        return self.get_queryset().search(query=query)


class Article(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    slug = models.SlugField(max_length= 50, blank=True, null= True, unique= True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    publish = models.DateField( auto_now_add= False, auto_now= False, null= True, blank= True)


    objects = ArticleManager()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})




def article_pre_save(sender, instance, *args, **kwargs):
 
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print(f'created: {created}')
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)
