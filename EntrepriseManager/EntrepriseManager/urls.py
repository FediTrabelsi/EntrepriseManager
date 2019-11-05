
from django.contrib import admin
from django.urls import path ,  include

urlpatterns = [
    path('', include('EntFrontend.urls')),
    path('', include('offres.urls')),
]
