from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=32)
    about=models.TextField()
    genre = models.CharField(max_length=32)
    published=models.BooleanField(default=True)
    year = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title