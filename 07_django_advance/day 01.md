1. 출생신고
2. master urls.py - path('', include('.urls')) -> urls 로 보내라

3. 새 앱에 urls.py 생성

   ```py
   from django.urls import path
   from . import views
   
   app_name = ''
   
   urlpatterns = [
       path('', views.index, name='index'),  # HOST/board/ == board:index
   ]
   ```

   

4. views에서 시작

   ```py
   from django.shortcuts import render
   
   def index(request):
       return render(request, '')
   ```

   

5. 앱에 templates안에 앱이름 + base.html

6. models.py -> `class Ar(models.Model):`



		1. 대충 table 만들겠다
  		2. ORM님 확인좀 makemigrations
  		3. 이대로 갑시다. migrate