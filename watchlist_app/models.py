from django.db import models

# Create your models here.


class StreamPlatform(models.Model):

    name=models.CharField(max_length=30)
    about=models.CharField(max_length=200)
    link=models.URLField(auto_created=100)
    
    def __str__(self):
        return self.name
    

class WatchList(models.Model):
    title = models.CharField(max_length=32)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    storyline=models.TextField()
    genre = models.CharField(max_length=32)
    published=models.BooleanField(default=True)
    year = models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    