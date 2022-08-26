from django.urls import path

from news.api.view import (article_list_create_api_view as articleListApiView, 
                            article_detail_create_api_view as articleDetailApiView)

urlpatterns = [
    path('articles', articleListApiView, name = 'article-list'),
    path('articles/<int:pk>', articleDetailApiView, name = 'article-detail'),
    
]