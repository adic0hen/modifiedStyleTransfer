from django.db import models
from django.utils import timezone
import os

# Create your models here.
class ContentPhoto(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='./static/images/content')
    file = models.FileField(default='NoName')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)


class StylePhoto(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='./static/images/style')
    file = models.FileField(default='NoName')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)

class ResultPhoto(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='./static/images/result')
    file = models.FileField(default='NoName')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)
