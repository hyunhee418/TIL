from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # DOMAIN/pages
    path('about/', views.about),  # DOMAIN/pages/about
    path('portfolio/', views.portfolio),  # DOMAIN/pages/portfolio
    path('help/', views.help),  # DOMAIN/pages/help
]