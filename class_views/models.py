"""Data models."""
from django.db import models


class PostModel(models.Model):
    """Published `post` data model"""

    id = models.AutoField(primary_key=True)
