from django.urls import path

from news.api.view import (ArticleDetailsView, ArticleListCreateView) 
# from news.api.view import (article_list_create_api_view as articleListApiView, 
                            # article_detail_create_api_view as articleDetailApiView)

urlpatterns = [
    # End-point for the class based view APIs
    path('articles', ArticleListCreateView.as_view(), name = 'article-list'),
    path('articles/<int:pk>/', ArticleDetailsView.as_view(), name = 'article-detail'),
    
    # End-point for the function based view APIs
    # path('articles', articleListApiView, name = 'article-list'),
    # path('articles/<int:pk>', articleDetailApiView, name = 'article-detail'),
    
]