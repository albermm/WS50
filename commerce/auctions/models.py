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
    

class Bids(models.Model):
    
    STATUS_CHOICES = [
    ('Open', 'Closed'),
    ('Won', 'Lost'),
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_id = models.AutoField(primary_key= True)
    amount = models.IntegerField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bid_id}: {self.listing}, bid: {self.amount}, status of the bid: {self.status}"


class Status(models.Model):
    OWN_CHOICES = [
    ('owner', 'watchlist'),
    ('Won', 'Lost'),
    ]
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    ownership= models.CharField(max_length=10, choices=OWN_CHOICES)
    listing = models.OneToOneField(Listings, on_delete=models.CASCADE)


