from django.urls import path
from . import views

app_name='movies'

urlpatterns=[
    path('', views.index, name='movie_index'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('create/', views.movie_create, name='movie_create'),
    path('<int:movie_id>/update', views.movie_update, name='movie_update'),
    path('<int:movie_id>/delete', views.movie_delete, name='movie_delete'),
    path('<int:movie_id>/reviews/create/', views.review_create, name='review_create'),
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.review_delete, name='review_delete'),
]