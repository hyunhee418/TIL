from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
# accounts에서 import 할 모든 함수 -> django.contrib.auth

from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
# accounts에서 import 할 Model(User), Form(UCF,AF)

from django.contrib.auth.decorators import login_required
# decorators

# 중요!
def signup(request):
    if request.user.is_authenticated:  # is_authenticated는 함수가 아님
        return redirect('article:article_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # logon을 합시다! 인자 2개
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form': form
    })



def login(request):
    if request.user.is_authenticated:  # is_authenticated는 함수가 아님
        return redirect('article:article_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # login 성공했으면 성공 유저 꺼내기
            user = form.get_user()
            # login을 합시다! 인자 2개
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form
    })


def logout(request):
    # auth_logout은 인자 1개
    auth_logout(request)
    return redirect('articles:article_list')