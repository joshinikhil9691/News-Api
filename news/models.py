from django.db import models


# Create your models here.

class Story(models.Model):
    headline = models.CharField(max_length=250)
    date = models.CharField(max_length=25)
    author = models.CharField(max_length=100)
    article = models.CharField(max_length=1000)
    link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.headline
