from offerRequirements.models import OfferRequirement
from rest_framework import viewsets, permissions
from .serializers import OffreRequirementSerializer

class OfferRequirementViewSet(viewsets.ModelViewSet):
    
    queryset = OfferRequirement.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    
    serializer_class= OffreRequirementSerializer

