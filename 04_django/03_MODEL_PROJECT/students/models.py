from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    github_id = models.CharField(max_length=50)
    age = models.IntegerField()

class Menu(models.Model):
    # name : 메뉴이름 STRING
    # price : 가격 FLOAT
    # category : 카테고리 STRING
    name = models.CharField(max_length=10)
    price = models.FloatField()
    category = models.CharField(max_length=10)