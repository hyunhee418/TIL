from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
# accounts에서 import 할 모든 함수 -> django.contrib.auth

from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
# accounts에서 import 할 Model(User), Form(UCF,AF)

from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# decorators
# Create your views here.

def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exist():
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')

@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles,
    })

@require_GET
def article_detail(request, article_id):
    # get_object_or_404의 1인자 모델명, 2인자 id=
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article':article,
    })

@login_required  # CRD는 모두 필요
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.id)

    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })

@login_required  # CRD는 모두 필요
@require_http_methods(['GET', 'POST'])
def article_update(request, article_id):
    # Update 추가사항
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. user 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')
    if request.method == 'POST':
        # 2. instance 주기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 고치기
            article = form.save()
            return redirect('articles:article_detail', article.id)

    else:
        # 4. 또 인스턴스 주기
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form,
    })
@login_required  # CRD는 모두 필요
@require_http_methods(['POST'])
def article_delete(request, article_id):
    # 주의! user 비교하기
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.user:
        article.delete()
    return redirect('articles:article_list')