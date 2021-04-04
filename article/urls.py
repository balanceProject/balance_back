from django.urls import path
from .views import (ArticleListAPIView, ArticleDetailAPIView, ImagesAPIView,
                    CategoryListAPIView)


urlpatterns = [
    path('', ArticleListAPIView.as_view()),
    path('<int:pk>', ArticleDetailAPIView.as_view()),
    path('image/', ImagesAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
]
