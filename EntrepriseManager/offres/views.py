from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Offer
from .serializers import OfferSerializer
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
def offer_by_ent_id(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            ent_id = post_data['id']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the entreprise"
                
                
                })
        else:
            offers = Offer.objects.filter(Entreprise = ent_id)
            serializer = OfferSerializer(offers, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "loading your offers",
                "offers" : serializer.data,
                
                })

@api_view(['POST',])
def create_offer(request):
    err_field=""
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            offer_name = post_data['name']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the name of the offer"
                })
            
        else:
            try :
                description = post_data['description']
            except:
                return JSONResponse({
                "success"  : False,
                "message":"you must provide a description for the the offer"
                })
            else:
                try:
                    nb_pos=post_data['nb_places']
                except:
                    return JSONResponse({
                "success"  : False,
                "message":"you must provide the number of available positions"
                })
                else:
                    try:
                        exp_date=post_data['ExpDate']
                    except:
                        return JSONResponse({
                "success"  : False,
                "message":"you must provide the expiration date"
                })
                    else :
                        try :
                            Entreprise=post_data['Entreprise']
                        except:
                            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the host entreprise"
                })
                        else:
                            if(((offer_name!="") and (description!="") and (nb_pos!="") and (exp_date!="") and (Entreprise!=""))):
                                serializer = OfferSerializer(data={
                                "name": offer_name,
                                "description" : description,
                                "nb_places" : nb_pos,
                                "ExpDate" : exp_date,
                                "Entreprise" : Entreprise
                                })
                                print(serializer)
                                if serializer.is_valid():
                                    offer= serializer.save()
                                    off = Offer.objects.filter(name = offer_name)
                                    offer_serializer = OfferSerializer(off, many=True)
                                    return JSONResponse({
                                        "success"  : True,
                                        "message" : "the offer "+offer_name+" was created",
                                        "data" :{ "offer" : offer_serializer.data[0]}
                                            })
                                else:
                                    return JSONResponse({
                                        "success"  : False
                                            })
                            else:
                                return JSONResponse({
                                    "success"  : False,
                                    "message" : "No field must be blank"})

            
            
            
@api_view(['POST',])
def delete_offer(request):
    if request.method == 'POST':        
        post_data = json.loads(request.body)
        try:
            offer_id = post_data['id']
        except:
            return JSONResponse({
            "success"  : False,
            "message" : "You must provide the id of the offer"
            })
        else:
            offer = Offer.objects.get(id = offer_id)
            offer.delete()
            return JSONResponse({
            "success"  : True,
            "message" : "offer was deleted"
            })
            
@api_view(['GET',])
def get_all_offers(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return JSONResponse({
                "success"  : True,
                "message"  : "All available offers : ",
                "offers" : serializer.data,
                
    })
    
        
@api_view(['POST',])
def offer_by_ent_name(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            ent_id = post_data['id'] 
            ent_name=post_data['name'] 
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the entreprise"
                
                
                })
        else:
            offers = Offer.objects.filter(Entreprise = ent_id)
            serializer = OfferSerializer(offers, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "The offers of "+ent_name+" are :",
                "offers" : serializer.data,
                
                })         

@api_view(['POST',])
def offer_by_skill(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            ent_id = post_data['id'] 
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the entreprise"
                
                
                })
        else:
            offers = Offer.objects.filter(Entreprise = ent_id)
            serializer = OfferSerializer(offers, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "The offers verifiying your search are : ",
                "offers" : serializer.data,
                
                })   