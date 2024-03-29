from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Student

@require_GET
def list(request):
    students = Student.objects.all()
    return render(request, 'classroom/list.html', {
        'students': students
    })

@require_GET
def detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/detail.html', {
        'student': student
    })

@require_GET
def new(request):
    return render(request, 'classroom/new.html')

@require_POST
def create(request):
    student = Student()
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect('classroom:detail', student.id)

@require_POST
def edit(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/edit.html', {
        'student':student
    })

@require_POST
def update(request, id):
    student = get_object_or_404(Student, id=id)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect('classroom:detail', student.id)

@require_POST
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('classroom:list')