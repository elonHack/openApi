from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default=" ")
    content = models.TextField()


    def __str__(self) -> str:
        return self.title