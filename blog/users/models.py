from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    matricNumber = models.CharField(max_length=20, unique=True)
    bio = models.TextField(blank=True, null=True)
    # USERNAME_FIELD = "email"  # Use email as the unique identifier
    profileImage = models.ImageField(
        upload_to="csc-421-blog/users/", null=True, blank=True
    )
    # username = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ["firstName", "lastName", "matricNumber"]

    def __str__(self):
        return self.email

    # objects = BlogUserManager()
