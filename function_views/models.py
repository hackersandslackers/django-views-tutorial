from django.db import models


class User(models.Model):
    """User account."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    profession = models.CharField(max_length=250, null=True)
    bio = models.TextField(null=True)
    location = models.CharField(max_length=250, null=True)
    twitter_profile = models.URLField(null=True)
    instagram_profile = models.URLField(null=True)
    avatar = models.CharField(max_length=250, null=True)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """Message left by a user in a guest book."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
