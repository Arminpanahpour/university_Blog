from django.db import models
from django.contrib.auth.admin import User
from blog.models import Post
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=220)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        # return reverse('detail-post', args=[self.slug])
        return reverse('detail-post', args=[self.post.id])
