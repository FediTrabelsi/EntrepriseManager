from rest_framework import serializers
from skills.models import skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta :
        model = skill
        fields = '__all__'

    def save(self):
        skills = skill(
            name=self.validated_data['name'],
            description= self.validated_data['description'],
        )
        skills.save()
        return skill
