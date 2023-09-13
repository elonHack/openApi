from django.db import models

# Create your models here.
class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    date = models.DateField(auto_now=True)