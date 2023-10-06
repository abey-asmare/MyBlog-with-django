from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField(max_length=300, blank=False, null=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.ManyToManyField('Comment', related_name='post', blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=False, default='default.jpg')

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def get_absolute_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=400, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-created_at', '-updated_at']


    def __str__(self):
        return f"user {self.owner} commented: {self.body}"



