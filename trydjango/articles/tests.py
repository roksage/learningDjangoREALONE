from django.test import TestCase
from .models import Article
# Create your tests here.
from .utils import slugify_instance_title

class ArticleTestCase(TestCase):
    
    def setUp(self) -> None:
        self.number = 5
        for n in range(0,self.number):
            Article.objects.create(title = 'hello world', content = 'blablabla')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number)

    def test_hello_world_slug(self):
        obj = Article.objects.all().first()
        slug = obj.slug
        self.assertEqual(slug, 'hello-world')


    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()  
        new_slugs = []

        for i in range(0,50000):
            instance = slugify_instance_title(obj, save = False)
            new_slugs.append(instance.slug)

        unique_slugs = list(set(new_slugs))

        self.assertEqual(len(new_slugs), len(unique_slugs))


    
    