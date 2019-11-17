from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Entreprise
from .serializers import EntrepriseSerializer , GetEntrepriseSerializer
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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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
                        print (post_data)

                        #{print((ent_name!="") and (password!="") and (password2!=""))
                        if(((ent_name!="") and (password!="") and (password2!=""))):
                            serializer = EntrepriseSerializer(data={
                            "name": ent_name,
                            "password" : password
                            })
                            if serializer.is_valid():
                                entreprise= serializer.save()
                                ent = Entreprise.objects.filter(name = ent_name)
                                ent_serializer = EntrepriseSerializer(ent, many=True)
                                return JSONResponse({
                                    "success"  : True,
                                    "message" : "the entreprise "+ent_name+" was created",
                                    "data" :{ "entreprise" : ent_serializer.data[0]}
                                        })
                        else:
                            return JSONResponse({
                                "success"  : False,
                                "message" : "No field must be blank",
                                    

                            
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
                        
                        ent = Entreprise.objects.filter(name=ent_name)
                        entserializer = GetEntrepriseSerializer(ent, many=True)
                        return JSONResponse({
                            "success"  : True,
                            "message" : "login into your account ...",
                            "data" :{ "entreprise" : entserializer.data[0]}
                            
                            })
                    else:
                        return JSONResponse({
                            "success"  : False,
                            "message" : "wrong password"
                            
                            })
        






def entreprise_list(request):
    if request.method == 'GET':
        entreprises= Entreprise.objects.all()

        serializer = GetEntrepriseSerializer(entreprises, many=True)
        return JSONResponse({
            "success"  : True,
            "message"  :  "All listed entreprises are :",
            "entreprises" : serializer.data,
            
            })


            
@api_view(['POST',])
def entreprise_by_name(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            ent_name = post_data['name']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the name of the entreprise"
                
                
                })
        else:
            entreprises = Entreprise.objects.filter(name = ent_name)
            serializer = GetEntrepriseSerializer(entreprises, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "loading your offers",
                "entreprise" : serializer.data,
                
                })

@api_view(['POST',])
def update_entreprise(request):
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
            entreprise = Entreprise.objects.filter(id = ent_id).update(moto= post_data['moto'])
            ent = Entreprise.objects.filter(id = ent_id)
            serializer = GetEntrepriseSerializer(ent, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "loading your offers",
                "entreprise" : serializer.data,
                
                })
