from django.urls import path, include
from .views import (ArticleHomeView, ArticleDetailView, ArticleUpdateView, ArticleCreateView,
                    ArticleDeleteView,ArticleDraftsListView, display_article_by_category_view, search_article)

app_name = 'blog'


urlpatterns = [

    path('', ArticleHomeView.as_view(), name='home'),
    path('article/<str:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('update-article/<str:slug>/',
         ArticleUpdateView.as_view(), name='update-article'),
    path('delete-article/<str:slug>/',
         ArticleDeleteView.as_view(), name='delete-article'),
    path('create-article/',
         ArticleCreateView.as_view(), name='create-article'),
    path('article-drafts/',
         ArticleDraftsListView.as_view(), name='draft-articles'),
    path('view-by-category/<str:slug>',
         display_article_by_category_view, name='view-article-by-category'),
    path('search-article/',
         search_article, name='search-article'),
]
