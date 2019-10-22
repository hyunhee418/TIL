from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostingForm, ImageForm
from .models import Posting, Image

# Create your views here.
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'postings/posting_detail.html', {
        'posting':posting,
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
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
    })

@require_POST
@login_required
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')