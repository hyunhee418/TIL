from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostingForm, ImageForm, CommentForm
from .models import Posting, Image, Comment, HashTag

# Create your views here.
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment_form = CommentForm()
    is_like = posting.like_users.filter(id=request.user.id).exists()

    return render(request, 'postings/posting_detail.html', {
        'posting':posting,
        'comment_form':comment_form,
        'is_like':is_like,
    })

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings':postings,
    })

@require_http_methods(['GET', 'POST'])
@login_required
def create_posting(request):
    images = request.FILES.getlist('file')
    if request.method == 'POST':
        # posting이 먼저 save
        posting_form = PostingForm(request.POST)
        if posting_form.is_valid() and len(images) <= 5:
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()
            
            words = posting.content.split()
            for word in words:
                if word[0] == '#':
                    tag = HashTag.objects.get_or_create(content=word)     # get_or_create 의 return이 list
                    posting.hashtags.add(tag[0])
            for image in images:    # 여러 개가 한번에 통과하지 못하므로 for문을 통해 하나씩 꺼내서 검사 후 save
                request.FILES['file'] = image  
                image_form = ImageForm(files=request.FILES)   # Form 류는 request로 시작하는 객체여야 사용가능.
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting
                    image.save()
            return redirect(posting)        

    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html', {
        'posting_form':posting_form,
        'image_form':image_form
    })

@require_http_methods(['GET', 'POST'])
@login_required
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if posting.author == request.user:
        if request.method == 'POST':
            posting_form = PostingForm(request.POST, instance=posting)
            if posting_form.is_valid():
                # posting = form.save(commit=False)
                # posting.author = request.user
                # 이미 채워져 있음
                posting = posting_form.save()
                return redirect(posting)
        else:
            posting_form = PostingForm(instance=posting)
    else:
        return redirect(posting)
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
    })

@require_POST
@login_required
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')

@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.posting = posting
        comment.save()
    return redirect(posting)

@login_required
@require_POST
def toggle_like(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    user = request.user

    # 좋아요를 누른 유저라면
    if posting.like_users.filter(id=user.id).exists():
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)
    return redirect(posting)