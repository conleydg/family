from django.db import models
from embed_video.fields import EmbedVideoField

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    video = EmbedVideoField()  # same like models.URLField()
    movie_date = models.DateField(null=True)
    upload_date = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=255, null=True)

class Tag(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)

class People(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.CharField(max_length=255)
