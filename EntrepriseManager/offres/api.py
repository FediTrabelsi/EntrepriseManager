from offres.models import Offer
from rest_framework import viewsets, permissions
from .serializers import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet):
    
    permission_classes=[
        permissions.AllowAny
    ]
    
    serializer_class= OfferSerializer

    def get_queryset(self):
        return self.request.entreprise.offers.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.entreprise)
    