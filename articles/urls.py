from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<slug:slug>/edit', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<slug:slug>/comment/', views.CommentCreateView.as_view(), name='comment_new')
]