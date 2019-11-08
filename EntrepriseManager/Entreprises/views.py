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
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.hashers import make_password,check_password
import bcrypt
# Create your views here.


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try : 
           ent_name = post_data['name']
        except:
            return JSONResponse({
                "success"  : False,
                "message" : "you have to provide the entreprise name"
                
                })
        else:
            try:
                password= post_data['password']
            except:
                return JSONResponse({
                "success"  : False,
                "message" : "you have to provide a password",
                
                })
            else:
                try:
                    password2= post_data['password2']
                except:
                    return JSONResponse({
                "success"  : False,
                "message" : "you have to provide password confirmation",
                
                })
                else:
                    if(password!=password2):
                        return JSONResponse({
                        "success"  : False,
                        "message" : "passwords dont match",
                        
                        })
                    else:
                        serializer = EntrepriseSerializer(data={
                            "name": ent_name,
                            "password" : password
                        })
                        if serializer.is_valid():
                            entreprise= serializer.save()
                            return JSONResponse({
                                "success"  : True,
                                "message" : "the entreprise "+ent_name+" was created",
                        
                                     })

@api_view(['POST',])
def login_view(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            ent_name = post_data['name']
        except:
            return JSONResponse({
                "success"  : False,
                "message" : "you have to provide the entreprise name"
                
                })
        else:
            entreprises = Entreprise.objects.filter(name = ent_name)
            serializer = EntrepriseSerializer(entreprises, many=True)
            if (len(serializer.data)== 0 ):
                return JSONResponse({
                "success"  : False,
                "message" : "Entreprise "+ent_name + " does not exists"
                })
            else:
                try:
                    password= post_data['password']
                except:
                    return JSONResponse({
                        "success"  : False,
                        "message" : "you need to provide password"
                        
                        })
                else:
                    hashed_pass = serializer.data[0]['password']
                    test = check_password(password,hashed_pass)
                    if(test):
                        return JSONResponse({
                            "success"  : True,
                            "message" : "login into your account ...",
                            
                            })
                    else:
                        return JSONResponse({
                            "success"  : False,
                            "message" : "wrong password"
                            
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
            "success"  : True,
            "entreprise" : serializer.data,
            
            })


            
@api_view(['POST',])
def entreprise_by_name(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        entreprises = Entreprise.objects.filter(name = post_data['name'])
        serializer = EntrepriseSerializer(entreprises, many=True)
        return JSONResponse({
            "success"  : True,
            "entreprise" : serializer.data,
            
            })
