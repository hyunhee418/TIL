from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),  # HOST/board/ == board:index
    # Read 글 목록(list)  render
    path('articles/', views.list, name='list'),
    # Read 글 상세(detail)  render
    path('articles/<int:id>/', views.detail, name='detail'),

    # Create  render
    path('articles/new/', views.new, name='new'),

    # Update  render
    path('articles/<int:id>/edit/', views.edit, name='edit'),

    # Delete 글 삭제(delete)
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]