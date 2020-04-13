from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForiegnKey('auth.user')
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=512)
    create_date = models.DateTimeField(timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

class Comments(models.Model):
    post = models.ForiegnKey('blog.Post',related_name='comments')
    author= models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
