from rest_framework import routers
from .api import SkillViewSet
from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
    url(r'^skills/getSkillById/', views.skillById),
    url(r'^skills/createSkill/', views.createSkill),
    url(r'^skills/deleteSkill/', views.deleteSkill),
    url(r'^skills/SkillsList', views.skills_list),

]