from django.db import models
from django.urls import reverse
from django.conf import settings  # Master_App/settings.py


from faker import Faker
f = Faker()
"""
삭제할 때 
$python manage.py migrate <Appname> zero
migration 된 것 최근 것부터 001까지 지움

$rm <Appname>/migrations/0*
0* -> 0으로 시작하는 것 전부 지운다 (__init__.py 빼고)

"""

class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # 이미지가 비워 있을 수 있다
    created_at = models.DateTimeField(auto_now_add=True) # 고정값
    updated_at = models.DateTimeField(auto_now=True) # 언제나 값이 바뀔 때 마다
    class Meta:  # column을 만드는 게 아니라 정보에 대한 내용이야
        ordering = ['-created_at',] # created_at을 descending 내림차순으로.
    
    # Detail 페이지를 쓸 거라면 만들어요.
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    
    def __str__(self):
        return f'{self.pk}:{self.content[:20]}'

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                content=f.sentence(),
                icon='fas fa-angrycreative',
                )
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name 이 없으면, posting.comment_set / 아래와 같다면 posting.comments
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# 바뀌면 무조건 makemigrations, migrate 하기
    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'

    @classmethod
    def dummy(cls, n, posting_id):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                posting_id=posting_id,
                content=f.sentence(),
                )
    