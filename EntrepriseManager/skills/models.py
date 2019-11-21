from django.db import models

# Create your models here.
class skill(models.Model):
    name= models.TextField(max_length=30, unique=True)
    description= models.TextField(max_length=100, null=True)
    
