from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout  # login 함수와 이름이 겹치니까

# login이 필요하다면 /accounts/login/ 으로 무조건 보냄 따라서 회원관련 함수는 accounts라는 앱이름과 login으로 지어야 함.
@require_http_methods(['GET', 'POST'])
def signup(request):  # new_user
    # 사용자가 회원가입할 데이터를 보냄
    if request.user.is_authenticated:     # 사용자가 로그인한 상태라면 무시하라
        return redirect('sns:posting_list')

    if request.method == 'POST':
       form = UserCreationForm(request.POST) 
       if form.is_valid():
           user = form.save()
           response =  redirect('sns:posting_list')  
        #    response.set_cookie(key='nickname', value='idiot', max_age=5)  # 만일 바로 return하면 mutable 해서 None이 return됨          
           return response


        # else:
        #     return render(request, 'accounts/signup.html', {
        #         'form':form
        #     })
    else:  # 사용자가 회원가입 HTML을 달라
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form':form
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:     # 사용자가 로그인한 상태라면 무시하라
        return redirect('sns:posting_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # 모든 modelform은 data를 첫번째 인자로 갖으나 유일하게 인증하는 애만 request가 첫번째 인자
        # form은 입국신청서의 의미
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('sns:posting_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form':form,
    })

def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')

