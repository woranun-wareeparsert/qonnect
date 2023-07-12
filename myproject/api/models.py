from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80) 
    age = models.IntegerField()
    
