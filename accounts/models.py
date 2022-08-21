from django.db import models
from django.contrib import auth

from posts.models import Post
# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    # post = models.ManyToManyField(Post, related_name='user_posts')

    def __str__(self):
        return "@{}".format(self.username)
