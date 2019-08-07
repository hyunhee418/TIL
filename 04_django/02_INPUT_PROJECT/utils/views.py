from django.shortcuts import render, redirect
from art import *
from .API import send_naver

def index(request):
    return render(request, 'utils/index.html')

def art(request):
    return render(request, 'utils/art.html', {
        'fonts': [
            "1row", "3-d", "3d_diagonal","alligator3", "alpha", 
            "acrobatic", "alphabet", "amcrazo2", "bear", 
            "dancingfont", "random",
            ],
    })

def output(request):
    user_input = request.GET.get('user-input')   # request.GET => dict like - GET 방식으로 날라온 요청에서 꺼내겠다.  
    user_font = request.GET.get('user-font')

    if user_input:
        result = text2art(user_input, font=user_font)
        return  render(request, 'utils/output.html', {
            'result': result,
        })

    else:
        return redirect('/utils/art')

def throw(request):
    return render(request, 'utils/throw.html')

def catch(request):
    name = request.GET.get('spot')
    menu = request.GET.get('menu')
    result = send_naver(name, menu)
    return render(request, 'utils/catch.html', result)

