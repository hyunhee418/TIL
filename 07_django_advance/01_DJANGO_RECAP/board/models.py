from django.db import models

class Article(models.Model):
    # id = models.IntegerField(primary_key=True)  안써도 테이블 생성 시 무조건 들어가게 되어있음
    title = models.CharField(max_length=100)  # 기본적으로 setting 값이 들어가있어 null=False와 같은 것은 굳이 쓸 필요 없음.
    content = models.TextField()
