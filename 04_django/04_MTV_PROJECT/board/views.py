from django.shortcuts import render, redirect   # redirect -> 새로고침
from .models import Article

# Create
def new(request):  # ti로운 게시글응 작성할 화면
    return render(request, 'board/new.html')

def create(request):  # 사용자 입력 데이터를 DB에 저장
    input_title = request.GET.get('input_title')
    input_content = request.GET.get('input_content')
    article = Article.objects.create(title=input_title, content=input_content)
    return redirect(f'/board/articles/{article.id}/')

# Read
def index(request):  # 모든 게시글 목록을 보여주는 view
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles
    })

def show(request, article_id):  # 특정 게시글을 보여주는 view
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html', {
        'article': article
    })

# Update
def edit(request):  # 특정 게시글을  수정핳 화면
    return render(request, 'board/edit.html')

# Delete
def delete(request, article_id):  # 특정 게시글을 삭제할 view(일)
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/articles/')