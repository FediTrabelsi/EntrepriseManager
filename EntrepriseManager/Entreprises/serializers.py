from rest_framework import serializers
from .models import Entreprise
from django.contrib.auth.hashers import make_password,check_password
import bcrypt

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('id','name', 'password')

    def save(self):
        entreprise = Entreprise(
            name=self.validated_data['name'],
            password= make_password(self.validated_data['password']),
        )
        entreprise.save()
        return entreprise

    
