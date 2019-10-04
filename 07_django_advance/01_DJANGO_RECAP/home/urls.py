from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('guess/', views.guess, name='guess'),  # HOST/home/hi
    path('', views.index, name='index'),    # HOST/home/
    path('answer/', views.answer, name='answer'),
]

