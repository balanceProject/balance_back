from django.contrib import admin
from .models import Article, Image, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('like',)
    list_display = ('title', 'created_at', 'updated_at', 'is_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
