"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from django_app import views, converters

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transport_list',views.transport_list),
    path('calcul_transport/<str:transport>/<float:km>',views.calcul_transport),
    path('recherche_transport/<str:transport>',views.recherche_transport),
    path('alimentation_list',views.alimentation_list),
    path('calcul_alimentation/<str:produit>/<float:g>',views.calcul_alimentation),
    path('recherche_alimentation/<str:produit>',views.recherche_alimentation),
    path('energie_list',views.energie_list),
    path('calcul_energie/<str:energie>/<float:km>',views.calcul_energie),
    path('recherche_energie/<str:energie>',views.recherche_energie)

]
