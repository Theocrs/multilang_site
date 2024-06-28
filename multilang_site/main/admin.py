from django.contrib import admin

from main.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publication_date')

admin.site.register(Article, ArticleAdmin)
