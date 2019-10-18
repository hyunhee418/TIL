from django.db import models
from django.urls import reverse

class Article(models.Model):
    # id = models.IntegerField(primary_key=True)  안써도 테이블 생성 시 무조건 들어가게 되어있음
    title = models.CharField(max_length=100)  # 기본적으로 setting 값이 들어가있어 null=False와 같은 것은 굳이 쓸 필요 없음.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):  # detail page가 있을 때
        return reverse("board:article_detail", kwargs={"article_id": self.id})
    
class Comment(models.Model):
    content = models.CharField(max_length=1000) # 1000이상 넘어가면 저장안함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # CASCADE => article을 삭제할 때 다같이 삭제하겠다.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
