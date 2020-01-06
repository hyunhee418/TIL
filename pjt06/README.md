# Project 06

## 1. 데이터베이스

먼저 프로젝트를 생성하고 movie라는 앱을 생성하였다.

이 후, 데이터베이스를 저장하기 위하여 movie앱에 models.py를 다음과 같이 구상하였다.

```python
from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})

class Review(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    
```

## 2. 페이지

앞서 만든 movie 앱의 url로 연결하기 위하여 master app의 urls.py에 `path('movies/', include('movies.urls')),`를 추가하였다.

또한 페이지를 만들기 이전에 pjt06에 templates/base.html을 만들고 settings.py에서 TEMPLATES 항목에 'DIRS': [os.path.join(BASE_DIR, 'templates')],를 넣어 프로젝트 전체에 중복되는 기본 값과 bootstrap을 가져오는 코드를 넣었다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/84a0eb3116.js" crossorigin="anonymous"></script>
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>
<div class="container">
    {% block body %}
    {% endblock body %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script> 
</div>
</body>
</html>
```

이 후, 영화 목록 페이지를 다음과 같이 구상하고, image를 넣어주기 위하여 앱 내에 static/movies/images/image.jpg를 만들고 목록페이지에 static을 로드하고 다음과 같이 작성하였다.

```html
{% extends 'base.html' %}
{% load static %}
{% block title %}Index{% endblock title %}

{% block body %}
    <h1 class="mx-auto mt-5" style="display:inline-block">영화 정보 조회</h1>
    <a href="{% url 'movies:movie_create' %}" class="btn btn-secondary">New</a>
    <img src="{% static 'movies/images/image.jpg'%}" alt="movie" class="rounded float-right mt-3" style="width:10rem">
    {% if movies %}
        <table class="table mt-3">
            <thead class="thead-dark"> 
                <tr>
                    <th>제목</th>
                </tr>
             </thead>
            <tbody>
            {% for movie in movies %}
                <tr>
                        <th scope="row"><a href="{% url 'movies:movie_detail' movie.id %}">{{movie.title}}({{movie.title_en}})</a></th>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    {% endif %}
{% endblock body %}
```

movie model form을 형성하기 위하여 forms.py를 다음과 같이 구상하였다.

```python
from django import forms
from .models import Movie, Review

class MovieModelForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField()
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.URLField()
    description = forms.Textarea()

    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewModelForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Review
        fields = ('score','content',)
```

이 후, 영화 조회, 수정, 삭제, 생성, 한줄평 삭제 및 생성까지 모두 구현하고자 urls.py와 views.py를 다음과 같이 생성하였다.

* urls.py

```python
from django.urls import path
from . import views

app_name='movies'

urlpatterns=[
    path('', views.index, name='movie_index'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('create/', views.movie_create, name='movie_create'),
    path('<int:movie_id>/update', views.movie_update, name='movie_update'),
    path('<int:movie_id>/delete', views.movie_delete, name='movie_delete'),
    path('<int:movie_id>/reviews/create/', views.review_create, name='review_create'),
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.review_delete, name='review_delete'),
]
```

* views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import MovieModelForm, ReviewModelForm


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {
        'movies':movies
    })

def movie_detail(request, movie_id):
    review_form = ReviewModelForm()
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all().order_by('-id')
    return render(request, 'movies/detail.html',{
        'movie':movie,
        'reviews':reviews,
        'review_form':review_form
    })

def movie_create(request):
    if request.method == 'POST':
        movie_form = MovieModelForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieModelForm()
    return render(request, 'movies/create.html', {
        'movie_form':movie_form
    })
def movie_update(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    if request.method == 'POST':
        movie_form = MovieModelForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieModelForm(instance=movie)
    return render(request, 'movies/create.html', {
        'movie_form':movie_form
    })

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    movie.delete()
    return redirect('movies:movie_index')

def review_create(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    form = ReviewModelForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.save()
    return redirect(movie)
        

def review_delete(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    review.delete()
    return redirect('movies:movie_detail', movie_id)
```



## 3. 페이지 구성

* _form.html

```html
<form method="POST">
    {% csrf_token %}
    {{movie_form.as_p}}
    <input type="submit">
</form>
```

* create.html

```python
{% extends 'base.html' %}
{% block title %}Create movie{% endblock title %}

{% block body %}
    <h1 class="mt-5 mb-3">New Movie</h1>
    {% include 'movies/_form.html' %}
{% endblock body %}
```

* detail.html

```html
{% extends 'base.html' %}
{% block title %}{% endblock title %}

{% block body %}
    <h1 class="mt-5 mb-3 text-center">{{movie.title}}({{movie.title_en}})</h1>
    <ul class="list-group mb-3">
        <li class="list-group-item">누적 관객수 : {{movie.audience}}</li>
        <li class="list-group-item">개봉일 : {{movie.open_date}}</li>
        <li class="list-group-item">장르 : {{movie.genre}}</li>
        <li class="list-group-item">관람등급 : {{movie.watch_grade}}</li>
        <li class="list-group-item">평점 : {{movie.score}}</li>
        <li class="list-group-item">포스터 이미지 URL : {{movie.poster_url}}</li>
        <li class="list-group-item">영화 소개 : {{movie.description}}</li>
    </ul>
    <div class="btn-group btn-group">
        <label class="btn btn-secondary">
            <a href="{% url 'movies:movie_index' %}"><button class="btn btn-secondary">목록</button></a>
        </label>
        <label class="btn btn-secondary">
            <a href="{% url 'movies:movie_update' movie.id %}"><button class="btn btn-secondary">수정</button></a>
        </label>
        <label class="btn btn-secondary">
            <form method="POST" action="{% url 'movies:movie_delete' movie.id %}">
                {% csrf_token %}
                <input class="btn btn-secondary" type="submit" value="삭제" onclick="return confirm('삭제하시겠습니까?')">
            </form>
        </label>
    </div>
    <hr>
    <div class="badge badge-secondary text-wrap text-center" style="font-size:2rem"> Review
    </div>

    <form method="POST" action="{% url 'movies:review_create' movie.id %}" class="mt-5">
        {% csrf_token %}
        {{review_form}}
        <input type="submit" class="btn btn-secondary float-right">
    </form>

    {% if reviews %}
    <ul class="mt-3" style="list-style:none">
        <li>
        <div class="row">
            <div class="col-0.5">
                Score
            </div>
            <div class="col-7">
                Content
            </div>
            <div class="col-3.5">
                Created_at
            </div>
            <div class="col-1"> 
            </div>
        </div>
        </li>
    </ul>
        <ul class="mt-3" style="list-style:none">
        {% for review in reviews %}
            <li>
            <div class="row">
                <div class="col-0.5">
                    {{review.score}}
                </div>
                <div class="col-7">
                    {{review.content}}
                </div>
                <div class="col-3.5">
                    {{review.create_at}}
                </div>
                <div class="col-1"> 
                    <form action="{% url 'movies:review_delete' movie.id review.id %}" method="POST">
                        {% csrf_token %}
                        <button class="btn btn-outline-danger btn-sm">X</button>            
                    </form>
                </div>
            </div>
            </li>
        {% endfor %}
        </ul>
    {% endif %}

{% endblock body %}
```

* update.html

```html
{% extends 'base.html' %}
{% block title %}Update movie{% endblock title %}

{% block body %}
    <h1 class="mt-3">Edit</h1>
    {% include '/movies/_form.html' %}
{% endblock body %}
```

## 4. 결과 및 고찰

이제까지 프로젝트를 하거나 수업을 들으면서 주도적으로 더 해보고 싶다거나 꾸미고 싶은 생각이 들진 않았었는데 이번 프로젝트는 처음으로 내가 만들고 싶은 대로 꾸미고 직접 구현해보면서 더 재미를 느낄 수 있었다.

