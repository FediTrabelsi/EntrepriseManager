from django.db import models

# Create your models here.

class Entreprise(models.Model):
    name = models.CharField(max_length=100)
    password= models.CharField(max_length=300,default="")
    description= models.CharField(max_length=500,default="")
    logo= models.CharField(max_length=100,default="")
    adress = models.CharField(max_length=100,default="")
    moto = models.CharField(max_length=100,default="")
    employees = models.IntegerField(null=True)
    capital = models.IntegerField(null=True)
    sector = models.CharField(max_length=100,default="")
    creationDate = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100,default="")
    phone = models.IntegerField(null=True)


    @classmethod
    def create(name, password):
        entreprise = cls(name= name , password= password)
        return entreprise