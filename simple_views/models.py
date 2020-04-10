from django.db import models
from datetime import datetime


class User(models.Model):
    """Data model representing user information."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    website = models.URLField()
    created_at = models.DateTimeField(default=datetime.now())


class Message(models.Model):
    """Data model representing messages left by users in a guest book."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
