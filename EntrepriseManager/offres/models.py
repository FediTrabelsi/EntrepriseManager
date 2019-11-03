from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Offer(models.Model):
    name= models.TextField(max_length=30, unique=True)
    description= models.TextField(max_length=100, null=True)
    nb_places= models.IntegerField(max_length=3)
    nb_applicants= models.IntegerField(max_length=3)
    CreationDate=models.DateTimeField(auto_now_add=True)
    ExpDate=models.DateTimeField(null=True)
    Status=models.BooleanField(null= True)



 