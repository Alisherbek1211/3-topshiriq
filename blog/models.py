from django.db import models
from author.models import User



class Category(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post/')
    content = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)
    min_read = models.CharField(max_length=255)
    is_popular = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    is_read_next = models.BooleanField(default=False)
    published_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

