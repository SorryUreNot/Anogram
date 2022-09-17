from django.db import models
from datetime import datetime
from django.utils.timezone import timezone


class post(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    datetime_create = models.DateTimeField(default=datetime.now())
