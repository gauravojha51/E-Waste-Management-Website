from django.db import models

# Create your models here.
class Feedback(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    feedback = models.TextField()
    date = models.DateField()
  
class Care(models.Model):
    first = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    address = models.TextField()
    electronic = models.CharField(max_length=30)
    items = models.CharField(max_length=6)
    date = models.DateField()