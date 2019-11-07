from rest_framework import serializers
from .models import Entreprise

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('id','name', 'password')


class RegistrationSerializer(serializers.ModelSerializer):

    password2= serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = Entreprise
        fields = ['name','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    def save(self):
        entreprise = Entreprise(
            name=self.validated_data['name'],
            password= self.validated_data['password'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        entreprise.save()
        return entreprise
