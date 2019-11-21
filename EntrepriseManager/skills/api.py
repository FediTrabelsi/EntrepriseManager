from skills.models import skill
from rest_framework import viewsets, permissions
from .serializers import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    
    queryset = skill.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    
    serializer_class= SkillSerializer

