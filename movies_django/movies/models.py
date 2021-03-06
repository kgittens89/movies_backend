from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    movie_poster = models.URLField()

    def __str__(self):
        return self.title
