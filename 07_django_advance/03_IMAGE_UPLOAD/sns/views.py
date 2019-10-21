from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

@require_GET
def posting_list(request):
    # nickname = request.COOKIES.get('nickname') 쿠키에서 정보 불러오기
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings':postings,
        # 'nickname':nickname
    })

@login_required  # login 이 x이면 무조건 accounts/login으로 무조건 가라 만일 이름을 accounts login이 싫다면 (login_url=)인자를 지정해줌 그러나 붙일 떄마다 해줘야해서 굳이 일을 두번할 필요 없음
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set이 아닌 이유는 related name = comments이기 때문
    is_like = True if posting.likes.filter(id=request.user.id).exists() else False
    return render(request, 'sns/posting_detail.html', {
        'posting':posting,
        'comments':comments,
        'is_like': is_like
    })
@login_required  # login 이 x이면 무조건 accounts/login으로 무조건 가라 만일 이름을 accounts login이 싫다면 (login_url=)인자를 지정해줌 그러나 붙일 떄마다 해줘야해서 굳이 일을 두번할 필요 없음
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():   # 검증
        posting = form.save(commit=False)   # 저장 => Posting 객체를 return
        posting.user = request.user  # anonymous일리가 없다 login_required 때문에
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page # redirect('sns:posting_detail', posting.id)

@login_required  # login 이 x이면 무조건 accounts/login으로 무조건 가라 만일 이름을 accounts login이 싫다면 (login_url=)인자를 지정해줌 그러나 붙일 떄마다 해줘야해서 굳이 일을 두번할 필요 없음
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')

@login_required  # login 이 x이면 무조건 accounts/login으로 무조건 가라 만일 이름을 accounts login이 싫다면 (login_url=)인자를 지정해줌 그러나 붙일 떄마다 해줘야해서 굳이 일을 두번할 필요 없음
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content만 값을 확인
    if form.is_valid():  # content만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있어서 저장하는 척만 하고 Comment객체를 return
        # comment.posting_id = posting.id
        comment.posting=posting # 객체 자체를 저장하면 알아서 id를 찾아서 넣음
        comment.user = request.user
        comment.save()
    return redirect(posting)

@login_required  # login 이 x이면 무조건 accounts/login으로 무조건 가라 만일 이름을 accounts login이 싫다면 (login_url=)인자를 지정해줌 그러나 붙일 떄마다 해줘야해서 굳이 일을 두번할 필요 없음
@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, posting_id=posting_id, id=comment_id)
    comment.delete()
    return redirect(posting)

@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    if posting.likes.filter(id=user.id).exists():
        posting.likes.remove(user)  # Delete
    else:
        posting.likes.add(user)   # Create
    return redirect(posting)

