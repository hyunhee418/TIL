from django import forms
from .models import Article

# forms.Form => Data 입력 및 검증
# form.ModelForm => Data 입력 및 검증 + HTML 생성

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)

    class Meta:
        model = Article
        fields = '__all__'