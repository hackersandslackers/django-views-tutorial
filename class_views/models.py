"""Data models."""
from django.db import models


class PostModel(models.Model):
    id = models.AutoField(primary_key=True)