from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
# TimeStampedModel -> created, modified가 자동으로 생김
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from django.contrib.auth import get_user_model
User = get_user_model()

class HashTag(TimeStampedModel):
    content = models.CharField(max_length=20, unique=True)  # 똑같은 애가 또 걸리면 저장

class Posting(TimeStampedModel):
    like_users = models.ManyToManyField(User, related_name='like_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings', blank=True)
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='postings')   # ManyToManyField -> 합쳐서 나올 테이블이 생김

    content = models.CharField(max_length=140)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("postings:posting_detail", kwargs={"posting_id": self.pk})
    

class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='images')
    file = ProcessedImageField(
        processors=[ResizeToFit(600, 600, mat_color=(256, 256, 256))],
        upload_to = 'postings/images/',
        format='JPEG',
        options={'quality': 90},
    )

# p = Posting.objects.last()
# p.image_set.all()  # related_name 이 default
# p.images.all()  # related_name이 images

class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')  # 남이 나를 어떻게 부를 것인가가 related_name
    content = models.CharField(max_length=140)

