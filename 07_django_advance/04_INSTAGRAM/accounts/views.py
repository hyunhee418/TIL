from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST

# 회원가입용 Form, 인증(로그인)용 Form
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# 현재 project에서 사용할 User 모델을 return하는 함수
from django.contrib.auth import login as auth_login, logout as auth_log_out

# from .models import User는 get_user_model을 써서 안써도 됨
from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form':form
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form
    })


def logout(request):
    auth_log_out(request)
    return redirect('/')

@require_GET
def user_page(request, user_id):
    user = get_object_or_404(User, id = user_id)
    return render(request, 'accounts/user_page.html', {
        'user_info' :user,
    })

def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)
    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)