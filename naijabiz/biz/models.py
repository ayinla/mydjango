from django.db import models

# Create your models here.
class Biz(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)

class Review(models.Model):
    review = models.CharField(max_length=100)
