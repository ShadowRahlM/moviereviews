from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(verbose_name="Date")


    def __str__(self) -> str:
        return self.headline
