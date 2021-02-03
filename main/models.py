from django.db import models


class File(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()
    Season = models.IntegerField()
    Episode = models.IntegerField()


class Main(models.Model):
    title = models.CharField(max_length=100)
    mainImg = models.ImageField(upload_to='main')
    Name = models.CharField(max_length=100)
    moreDesc = models.TextField()


class Character(models.Model):
    title = models.CharField(max_length=100)
    ChrImage = models.ImageField(upload_to="characters")
    name = models.CharField(max_length=100)
    description = models.TextField()


class Picture(models.Model):
    title = models.CharField(max_length=100)
    Pic = models.ImageField(upload_to='picture')