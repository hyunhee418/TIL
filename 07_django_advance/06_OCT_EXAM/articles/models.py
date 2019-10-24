from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Article(models.Model):
    # ForeignKey, 두 번째 인자: on_delete=models.CASCADE
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내가 뭐라고 접근할 지 ...... related_name=남이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name="like_articles")