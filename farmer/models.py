from django.db import models
from django.contrib.auth.models import User

class LatestPost(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.CharField(max_length=200)
class Schemes(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()


# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    land = models.IntegerField()
    aadhar_ID= models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    crop = models.CharField(max_length=30,default="Wheat")


class Merchandiser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=50)
    aadhar_ID= models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
