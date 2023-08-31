from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    bio = models.TextField()
