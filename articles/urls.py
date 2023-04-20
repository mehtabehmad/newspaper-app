from django.urls import path

from django.views.generic import ListView

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    )

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('atricle_new/', ArticleCreateView.as_view(), name="article_new"),
]