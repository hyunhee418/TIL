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
    