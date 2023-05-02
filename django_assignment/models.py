from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = [
        (YOUTUBE, 'YouTube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]
    link = models.URLField(max_length=255)
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)
