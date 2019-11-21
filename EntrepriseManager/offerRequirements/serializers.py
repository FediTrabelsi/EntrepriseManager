from rest_framework import serializers
from .models import OfferRequirement

class OffreRequirementSerializer(serializers.ModelSerializer):
    class Meta :
        model = OfferRequirement
        fields = '__all__'

    def save(self):
        offerRequirements = OfferRequirement(
            skill=self.validated_data['skill'],
            offer= self.validated_data['offer'],
        )
        offerRequirements.save()
        return offerRequirements
