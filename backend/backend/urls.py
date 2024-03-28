from django.contrib import admin
from django.urls import path, register_converter
from django_app import views, converters

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transport_list/',views.transport_list),
    path('calcul_transport/<str:transport>/<float:km>/',views.calcul_transport),
    path('recherche_transport/<str:transport>/',views.recherche_transport),
    path('alimentation_list/',views.alimentation_list),
    path('calcul_alimentation/<str:produit>/<float:g>/',views.calcul_alimentation),
    path('recherche_alimentation/<str:produit>/',views.recherche_alimentation),
    path('categorie_alimentation/',views.categorie_alimentation),
    path('select_categorie/<str:categorie>/',views.select_categorie),
    path('select_sous_categorie/<str:sous_categorie>/',views.select_sous_categorie),
    path('energie_list/',views.energie_list),
    path('calcul_energie/<str:energie>/<float:kwh>/',views.calcul_energie),
    path('recherche_energie/<str:energie>/',views.recherche_energie)

]
