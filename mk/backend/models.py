from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    cover_url = models.URLField(max_length=200)
    plot = models.CharField(max_length=500)
    full_time = models.DateTimeField()

class Movies_Shot(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    video_url = models.URLField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    movies = models.ForeignKey('Movies', on_delete=models.CASCADE)

