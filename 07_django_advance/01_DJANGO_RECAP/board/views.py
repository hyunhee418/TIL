from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import ArticleModelForm
from .models import Article

from IPython import embed

# CRUD
@require_http_methods(['GET', 'POST'])
def new(request):
    # 요청이 GET/POST인지 확인한다.
    # 만약 POST 라면
    if request.method == 'POST':
        pass
        # ArticleModelForm의 인스턴스를 생성하고 Data를 채운다(binding).
        form = ArticleModelForm(request.POST)
        # binding된 form이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form을 저장한다.
            article = form.save()
            # 저장한 article로 redirect한다.
            return redirect(article)
        # # form이 유효하지 않다면
        # else:
        #     # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자한테 보여준다.
        #     return render(request, 'board/new.html', {
        #         'form': form
        #     })
    # 만약 GET이라면
    else:
        # 비어있는 form(HTML 생성기)을 만든다.
        form = ArticleModelForm()
        # form과 html을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form':form
    })

@require_GET
def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles
    })

@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/detail.html', {
        'article': article
    })

@require_http_methods(['GET', 'POST'])
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method =='POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {
        'form': form,
    })

@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')

def index(request):
    pass











# from .models import Article
# from .forms import ArticleModelForm

# @require_GET
# def index(request):
#     return render(request, 'board/index.html')

# @require_GET
# def list(request):
#     articles = Article.objects.all()
#     return render(request, 'board/list.html', {
#         'articles':articles,
#     })

# @require_GET
# def detail(request, id):
#     article = get_object_or_404(Article, id=id)
#     return render(request, 'board/detail.html', {
#         'article' : article,
#     })


# def new(request):
#     if request.method == "POST":
#         form = ArticleModelForm(request.POST)       
#         if form.is_valid():
#             article = form.save()
#             return redirect(article)
#     else:
#         form = ArticleModelForm()

#     return render(request, 'board/new.html', {
#         'form':form,
#     })


# def edit(request, id):
#     article = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#         return redirect(article)
#     else:
#         return render(request, 'board/edit.html', {
#             'article': article
#         })

# @require_POST
# def delete(request, id):
#     article = get_object_or_404(Article, id=id)
#     article.delete()
#     return redirect('board:list')