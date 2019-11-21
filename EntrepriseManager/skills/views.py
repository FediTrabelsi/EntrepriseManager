from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import skill
from .serializers import SkillSerializer
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
def skillById(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            skill_id = post_data['id']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the id of the skill"
                })
        else:
            skills = skill.objects.filter(id = skill_id)
            serializer = SkillSerializer(skills, many=True)
            return JSONResponse({
                "success"  : True,
                "message"  : "loading your skills",
                "skills" : serializer.data,
            }) 


@api_view(['POST',])
def createSkill(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        try:
            skill_name = post_data['name']  
        except:
            return JSONResponse({
                "success"  : False,
                "message":"you must provide the name of the skill"
                })
            
        else:
            try :
                description = post_data['description']
            except:
                return JSONResponse({
                "success"  : False,
                "message":"you must provide a description for the the skill"
                })
            else:
                if(((skill_name!="")and (description!=""))):
                    serializer = SkillSerializer(data={
                    "name": skill_name,
                    "description" : description
                     })
                    print(serializer)
                    if serializer.is_valid():
                        skill= serializer.save()
                        skill= skill.objects.filter(name = skill_name)
                        skill_serializer = SkillSerializer(skill, many=True)
                        return JSONResponse({
                        "success"  : True,
                        "message" : "the Skill "+skill_name+" was created",
                        "data" :{ "skill" : skill_serializer.data[0]}
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
def deleteSkill(request):
    if request.method == 'POST':        
        post_data = json.loads(request.body)
        try:
            skill_id = post_data['id']
        except:
            return JSONResponse({
            "success"  : False,
            "message" : "You must provide the id of the skill"
            })
        else:
            skilld = skill.objects.get(id = skill_id)
            skilld.delete()
            return JSONResponse({
            "success"  : True,
            "message" : "skill was deleted"
            })


@api_view(['GET',])
def skills_list(request):
    if request.method == 'GET':
        skills= skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return JSONResponse({
            "success"  : True,
            "skills" : serializer.data
        })
        
                   
                    
            