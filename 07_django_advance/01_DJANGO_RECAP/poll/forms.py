from django import forms
from .models import Question, Choice

class ChoiceModelForm(forms.ModelForm):
    CHOICES = [
        ('한식', '한식임'),
        ('중식', '중심임'),
        ('양식', '양식임'),
    ]
    content = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Choice
        fields = ('content',)