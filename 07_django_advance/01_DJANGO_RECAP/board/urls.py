from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),  # HOST/board/ == board:index
    # Read 글 목록(list)  render
    path('articles/', views.article_list, name='article_list'),
    # Read 글 상세(detail)  render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # Create  render
    path('articles/new/', views.new_article, name='new_article'),

    # Update  render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),

    # Delete 글 삭제(delete)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    
    # Create Comment
    # 1:N관계 -> 주인이 먼저 나옴
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),

    # Delete Comment
    path('articles/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]