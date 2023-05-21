from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = "user_bid")

    def __str__(self):
        return f"Bid {self.bid} by {self.user}"

class Listing(models.Model):
    title = models.CharField(max_length = 32)
    description = models.CharField(max_length = 256)
    image_url = models.CharField(max_length = 1024)
    price = models.ForeignKey(Bid, on_delete = models.CASCADE, blank = True, null = True, related_name = "bid_amount")
    active = models.BooleanField(default = True)
    owner = models.ForeignKey(User, related_name = "user", null = True, blank = True, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, related_name = "user", null = True, blank = True, on_delete = models.CASCADE)
    watchlist = models.ManyToManyField(User, blank = True, null = True, related_name = "watchlist")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commenter = models.ForeignKey(User, related_name = "commenter", null = True, blank = True, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, related_name = "listing", null = True, blank = True, on_delete = models.CASCADE)
    message = models.CharField(max_length = 256)

    def __str__(self):
        return f"{self.commenter}: {self.message[:8]}..."