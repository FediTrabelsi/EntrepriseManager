from rest_framework import routers
from .api import OfferRequirementViewSet
from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
    url(r'^offerRequirements/getOfferRequirementById/', views.offerRequirementById),
    url(r'^offerRequirements/createOfferRequirement/', views.createOfferRequirement),
    url(r'^offerRequirements/deleteOfferRequirement/', views.deleteOfferRequirement),

]