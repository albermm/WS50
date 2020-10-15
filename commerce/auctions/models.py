from django.contrib.auth.models import AbstractUser
from django.db import models
#from . import models


class User(AbstractUser):
    pass


class Listings(models.Model):
    listing_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    startingbid = models.IntegerField()
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.listing_id}: {self.title}, description: {self.description}, initial bid: {self.startingbid}, category: {self.category}"
    