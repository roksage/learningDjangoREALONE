from django.contrib import admin

# Register your models here.


from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'content', 'id', 'timestamp']
    sortable_by = ['title']
admin.site.register(Article,ArticleAdmin)