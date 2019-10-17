from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('<int:question_id>/new_vote/', views.new_vote, name='new_vote')
]
