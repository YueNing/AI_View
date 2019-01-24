###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Last Change Datum: 16.01.2019
# Location: KIT
# File_Name: backend module
# E-mail: n1085633848@gmail.com
###############################

from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    title_id = models.CharField(max_length=10)
    genres = models.CharField(max_length=30)
    themes = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    cover_url = models.URLField(max_length=200)
    plot = models.CharField(max_length=500)
    full_time = models.DurationField()

    def __str__(self):
        return '{}'.format(self.title)

class Movies_Shot(models.Model):
    shot_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100) 
    genre = models.CharField(max_length=30)
    video_url = models.URLField(max_length=200)
    start_time = models.DurationField()
    end_time = models.DurationField()
    caption = models.CharField(max_length=250)
    movies = models.ForeignKey('Movies', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}:{}'.format(self.title, self.shot_id)

