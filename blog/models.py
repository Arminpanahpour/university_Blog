from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True, null=True)
    header_image = models.ImageField(blank=True, null=True, upload_to='images/')
    body = models.TextField()
    category = models.CharField(max_length=220, default='category')
    likes = models.ManyToManyField(User, related_name='blog_post', blank=True)

    def get_absolute_url(self):
        return reverse('detail-post', args=[self.slug])

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
