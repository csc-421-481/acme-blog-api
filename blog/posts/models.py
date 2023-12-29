from django.db import models
from users.models import BlogUser


class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    REQUIRED_FIELDS = ["name", "color"]


class Post(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    coverImage = models.ImageField(
        upload_to="csc-421-blog/posts/cover-images", null=True, blank=True
    )
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    # REQUIRED_FIELDS = ["title", "coverImage"]


class Comment(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
