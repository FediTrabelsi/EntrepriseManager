from django.conf.urls import url
from . import views
from django.urls import path
from .views import( registration_view,)

urlpatterns = [
    url(r'^entreprises/getAll', views.entreprise_list),
    url(r'^entreprises/getByName/$', views.entreprise_by_name),
]