from django.db import models

# Create your models here.

class Entreprise(models.Model):
    name = models.CharField(max_length=100)
    password= models.CharField(max_length=300,default="")


    @classmethod
    def create(name, password):
        entreprise = cls(name= name , password= password)
        # do something with the book
        return entreprise