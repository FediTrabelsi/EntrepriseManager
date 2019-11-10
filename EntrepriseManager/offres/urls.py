from rest_framework import routers
from .api import OfferViewSet
from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^offers/getByEntId/', views.offer_by_ent_id),
    url(r'^offers/createOffer/', views.create_offer),
    url(r'^offers/deleteOffer/', views.delete_offer),

]
