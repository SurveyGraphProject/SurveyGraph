from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=400)
    year = models.IntegerField()
    url = models.CharField(max_length=2048)
    
    # Authors = 
    # references_from = # List of article ids
    # references_to = # List of article ids

# class Authors():