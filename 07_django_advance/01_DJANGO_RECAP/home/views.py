from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')


def guess(request):
    return render(request, 'home/guess.html')

def answer(request):
    count = 0
    if request.GET.get('q1') == '1992-04-18':
        count += 1
    if request.GET.get('q2') == '힙합':
        count += 1
    if request.GET.get('q3') == '옹돌이':
        count += 1
    print(request.GET.get('q1'))

    return render(request, 'home/answer.html', {'count':count})