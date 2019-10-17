from django import forms
from .models import Article, Comment

# forms.Form => Data 입력 및 검증 + HTML 생성 => Model 정보를 모름
# form.ModelForm => Data 입력 및 검증 + HTML 생성 => Model 정보를 알고있음

# Ref
# class ArticleForm(forms.Form):  # 검증용 모든 Data에 대하여 검증할 애를 다 써줘야 함
#     title = forms.CharField(min_length=2, max_length=100)
#     content = forms.CharField()

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)

    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=1000)
    # 200 넘어가면 에러 (200이하임을 검증)

    class Meta:
        model = Comment
        fields = ('content',)   # model form이 검증할 때 id는 안보고 content만 확인할께
        # 입력검증도 content만 하지만, 새로 생성도 content만 한다. 따라서, 댓글에 적합