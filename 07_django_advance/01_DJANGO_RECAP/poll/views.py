from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from .forms import ChoiceModelForm

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = ChoiceModelForm()
    choices = question.choice_set.all()
    return render(request, 'poll/question_detail.html', {
        'question':question,
        'form':form,
        'choices':choices,
    })

def new_vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = ChoiceModelForm(request.POST)
    choices = question.choice_set.all()
    if form.is_valid():
        choice = form.save(commit=False)
        for ch in range(len(choices)):
            if choices[ch].content == choice.content:
                choices[ch].votes += 1
                choices[ch].save()
    return redirect('poll:question_detail', question.id)