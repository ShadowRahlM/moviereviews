from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='movies/images/')
    url = models.URLField(blank=True)
    date = models.DateField()


    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    text = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField(default=False)


    def __str__(self):
        return self.text