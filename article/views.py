from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ArticleListSerializer, CategoryListSerializer, ImagesSerializer
from .models import Article, Category, Image


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['category']


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ImagesAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
