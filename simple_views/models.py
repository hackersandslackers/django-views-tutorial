from django.db import models


class User(models.Model):
    """Data model representing user information."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    title = models.CharField(max_length=250, null=True)
    bio = models.TextField(null=True)
    location = models.CharField(max_length=250, null=True)
    avatar = models.CharField(max_length=250, null=True)
    website = models.URLField()
    created_at = models.DateTimeField()


class Message(models.Model):
    """Data model representing messages left by users in a guest book."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField()
