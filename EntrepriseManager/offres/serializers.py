from rest_framework import serializers
from offres.models import Offer

class OfferSerializer(serializers.ModelSerializer):
    class Meta :
        model = Offer
        fields = '__all__'

    def save(self):
        offer = Offer(
            name=self.validated_data['name'],
            description= self.validated_data['description'],
            nb_places= self.validated_data['nb_places'],
            ExpDate= self.validated_data['ExpDate'],
            Entreprise= self.validated_data['Entreprise'],
        )
        offer.save()
        return offer
