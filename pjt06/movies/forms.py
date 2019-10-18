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

