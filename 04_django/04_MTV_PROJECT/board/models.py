from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # 처음 들어갔을 때 저장됨.
    modified = models.DateTimeField(auto_now=True)  # 바뀔때마다 자동으로 바뀌면서 저장됨.

    def __str__(self):
        return f'{self.id}: {self.title}'