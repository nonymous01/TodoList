from django.db import models

# Create your models here.

class Article(models.Model):
    description = models.CharField(max_length=200)
    titre= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.titre