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