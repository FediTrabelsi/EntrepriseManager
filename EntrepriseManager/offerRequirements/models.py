from django.db import models
from skills.models import skill
from offres.models import Offer 

# Create your models here.
class OfferRequirement(models.Model):
    skill = models.ForeignKey(skill, on_delete=models.DO_NOTHING ,default="")
    offer = models.ForeignKey(Offer , on_delete=models.CASCADE, default="")