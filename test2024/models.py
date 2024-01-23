from django.db import models

# Create your models here.

# prompt/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Test2024(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test2024 = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)