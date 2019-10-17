from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import ArticleModelForm, CommentModelForm
from .models import Article, Comment

from IPython import embed


# Ref
# Create Article with Form
# def new_article_with_form(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = Article()
#             # article.title = request.POST.get('title')  # 검증되지 않은 데이터 쓰면 안됨 -> 오염된 Data가 들어갈 수 있음
#             article.title = form.cleaned_data.get('title')  # cleaned_data => 검증된 데이터
#             article.content = form.cleaned_data.get('content')
#             article.save()
#             # title = form.cleaned_data.get('title')
#             # content = form.cleaned_data.get('content')
#             # article = Article.objects.create(title=title, content=content)
#             return redirect(article)
#     else:
#         form = ArticleForm()
#     return render(request, 'board/new.html', {
#         'form': form,
#     })


# CRUD
@require_http_methods(['GET', 'POST'])
def new_article(request):
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
        #     return render(request, 'board/new_article.html', {
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
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles
    })

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all().order_by('-id')  # 모든 comment를 역순으로 주세요
    comment_form = CommentModelForm()
    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form' : comment_form,
    })

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
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
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')

@require_POST
def new_comment(request, article_id):  # /board/articles/N/comments/new/
    article = get_object_or_404(Article, id=article_id)  # 검증(id가 있는지)
    form  = CommentModelForm(request.POST)  # form에 article_id가 없음
    # embed()
    if form.is_valid():
        # form.save()# HTML에 저장한 애를 하나 잡아서 내보낼 필요 없으니까 comment=form.save()가 아니라 저장만 함 
        comment = form.save(commit=False)   # 근데 article_id가 없어서 저장이 안됨.. 'commit=False'는 가상으로 저장해놓을께
        comment.article_id = article.id   # 이건 직접 넣어줄께
        comment.save()   # 진짜 save
    return redirect(article)  # 실패해도 어짜피 redirect이므로 else 필요 없음

@require_POST
def delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)
    # comment_id도 같고 article_id도 같은 애를 찾으면 더 빨라짐
    
    # 안전하고 빠르지 않은 경우 
    # comment = get_object_or_404(Comment, id=comment_id)
    # if comment in article.comment_set.all():
        # SELECT * FROM articles WHERE id=article_id 너무 오래걸림

    comment.delete()
    return redirect(article)

    
    # comment.delete()
    # return redirect(comment.article)  # 지워지는 건 db에서 지워지는 것이므로 python 메모리에는 남아있음

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