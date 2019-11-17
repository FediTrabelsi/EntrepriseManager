from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^entreprises/getAllEntreprises', views.entreprise_list),
    url(r'^entreprises/updateEntreprise', views.update_entreprise),
    url(r'^entreprises/getByName/$', views.entreprise_by_name),
    url(r'^entreprises/login/$', views.login_view),
    url(r'^entreprises/register/$', views.registration_view),

]