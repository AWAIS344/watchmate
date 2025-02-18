from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

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
    
class Reviews(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment=models.CharField(max_length=100)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title

