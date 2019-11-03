from offres.models import Offer
from rest_framework import viewsets, permissions
from .serializers import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset= Offer.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]

    serializer_class= OfferSerializer