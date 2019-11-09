
from django.contrib import admin
from django.urls import path ,  include
from django.urls import path, re_path, include
from Entreprises.views import registration_view

urlpatterns = [
    path('', include('EntFrontend.urls')),
    path('', include('offres.urls')),
    path('',include('Entreprises.urls')),
    path('admin/', admin.site.urls),
]
