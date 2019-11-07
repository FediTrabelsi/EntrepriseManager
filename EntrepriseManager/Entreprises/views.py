from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Entreprise
from .serializers import EntrepriseSerializer
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            entreprise = serializer.save()
            data['response']= "Entreprise succesfully registred"
            data['name']= entreprise.name
            data['password']= entreprise.password
        else:
            data= serializer.errors
        return Response({
            "data":data,
            "token": "w8"
            })



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def entreprise_list(request):
    if request.method == 'GET':
        entreprises= Entreprise.objects.all()

        serializer = EntrepriseSerializer(entreprises, many=True)
        return JSONResponse({
            "entreprise" : serializer.data,
            
            })

            
@api_view(['POST',])
def entreprise_by_name(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        entreprises = Entreprise.objects.filter(name = post_data['name'])
        serializer = EntrepriseSerializer(entreprises, many=True)
        return JSONResponse({
            "entreprise" : serializer.data,
            
            })
