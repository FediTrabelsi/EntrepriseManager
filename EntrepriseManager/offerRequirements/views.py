from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import OfferRequirement
from .serializers import OffreRequirementSerializer
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST',]) 
def offerRequirementById(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            offerRequirement_id = post_data['id']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the offerRequirement"
                })
        else:
            offerRequirements = offerRequirement.objects.filter(id = offerRequirement_id)
            serializer = OfferRequirementSerializer(offerRequirements, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "loading your skills",
                "offerRequirement" : serializer.data,
            }) 

@api_view(['POST',])
def createOfferRequirement(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            skill_id = post_data['skill']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the skill"
                })
            
        else:
            try :
                offer_id = post_data['offer']
            except:
                return JSONResponse({
                "success"  : False,
                "message":"you must provide the id for the the offer"
                })
            else:
                if(((skill_id!="")and (offer_id!=""))):
                    serializer = OffreRequirementSerializer(data={
                    "skill": skill_id,
                    "offer" : offer_id
                     })
                    print(serializer)
                    if serializer.is_valid():
                        offerRequirement= serializer.save()
                        offerRequirement_serializer = OffreRequirementSerializer(offerRequirement, many=True)
                        return JSONResponse({
                        "success"  : True,
                        "message" : "the offerRequirement was created",
                        "data" :{ "offerRequirement" : offerRequirement_serializer.data[0]}
                        })
                    else:
                        return JSONResponse({
                        "success"  : False,
                        "message"  : "OfferRequirement Could not be created"
                        })      
                else:
                    return JSONResponse({
                    "success"  : False,
                    "message" : "No field must be blank"})

@api_view(['POST',])
def deleteOfferRequirement(request):
    if request.method == 'POST':        
        post_data = json.loads(request.body)
        try:
            offerRequirement_id = post_data['id']
        except:
            return JSONResponse({
            "success"  : False,
            "message" : "You must provide the id of the offerRequirement"
            })
        else:
            OfferRequirementd = OfferRequirement.objects.get(id = offerRequirement_id)
            OfferRequirementd .delete()
            return JSONResponse({
            "success"  : True,
            "message" : "offerRequirement was deleted"
            })
            