from django.db import models
from s3direct.fields import S3DirectField

class MovieInfo(models.Model):
    movie_name=models.CharField(max_length=200)
    movie_review = models.CharField(max_length=3)
    movie_release_date = models.CharField(max_length=20)
    movie_type = models.CharField(max_length=50)
    movie_detail = models.TextField(max_length=500)
    image=models.ImageField(upload_to="pictures",blank=True,null=True)


    def __str__(self):
        return self.movie_name

class Our_images(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    image_url = models.ImageField(upload_to="our_pictures", blank=True, null=True)

    def __str__(self):
        return self.name




    # def __str__(self):

