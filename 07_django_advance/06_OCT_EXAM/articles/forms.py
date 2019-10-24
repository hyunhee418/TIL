from django import forms
from .models import Article

# forms / models 앞은 s가 붙고, Form / Model은 안붙
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)