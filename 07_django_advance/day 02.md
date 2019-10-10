1. app 만들고 출생신고

2. ulrs에 include 추가하고 path('classroom/', include('classroom.urls')),

3. urls 만들기

4. urls에 

   ```py
   from django.urls import path, include
   from . import views
   
   app_name = 'classroom'
   
   urlpatterns = [
       path('students/', views.list, name='list')
   ]
   ```

   

5. views

   ```py
   from django.shortcuts import render, redirect, get_object_or_404
   from .models import Student
   
   def list(request):
       students = Student.objects.all()
       return render(request, 'classroom/list.html', {
           'students': students
       })
   ```

   

6. models

   ```py
   from django.db import models
   
   class Student(models.Model):
       name = models.CharField(max_length = 10)
       age = models.IntegerField()
       major = models.TextField()
   ```

   

7. DB 생성

   `$ python manage.py makemigrations classroom`

   `$ python manage.py migrate classroom`

8. html 생성

   html 내 students 이용







Admin

1. $ python manage.py migrate

2. $ python manage.py createsuperuser

3. 이름, 비밀번호 등록

4. app의 admin.py에서 

   ```py
   from .models import Article
   
   class ArticleModelAdmin(admin.ModelAdmin):
       list_display = 'id', 'title'
   
   admin.site.register(Article)
   ```

   

