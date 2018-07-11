from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=160)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=0)