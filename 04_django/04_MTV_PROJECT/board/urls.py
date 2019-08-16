from django.urls import path
from . import views

urlpatterns = [
   
    # Create
    path('articles/new/', views.new),   # DOMAIN/board/articles/new
    # Read
    path('articles/', views.index),   # DOMAIN/board/articles
    path('articles/<int:article_id>/', views.show),    # DOMAIN/board/articles/1
    path('articles/create/', views.create),   # DOMAIN/board/articles/create
    path('articles/<int:article_id>/delete/', views.delete),    # DOMAIN/board/articles/delete
    # Update
    # Delete
]
