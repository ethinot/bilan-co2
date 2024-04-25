# views.py
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django_app.models import BD

tr = BD("transport.csv")
al = BD("alimentation.csv")
en = BD("energie.csv")

def calcul_transport(request,transport:str,km:float):
    if request.method == 'GET':
        return calcul(tr,transport,km)

def calcul_alimentation(request,produit:str,g:float):
    if request.method == 'GET':
        return calcul(al,produit,g)


def calcul_energie(request,energie:str,kwh:float):
    if request.method == 'GET':
        return calcul(en,energie,kwh)


def transport_list(request):
    if request.method == 'GET':
        return JsonResponse(tr.list_value(),safe=False)
def alimentation_list(request):
    if request.method == 'GET':
        return JsonResponse(al.list_value(),safe=False)
def energie_list(request):
    if request.method == 'GET':
        return JsonResponse(en.list_value(),safe=False)


def recherche_transport(request,transport:str):
    if request.method == 'GET':
        return JsonResponse(tr.recherche(transport),safe=False)

def recherche_alimentation(request,produit:str):
    if request.method == 'GET':
        return JsonResponse(al.recherche(produit),safe=False)
    
def recherche_energie(request,energie:str):
    if request.method == 'GET':
        return JsonResponse(en.recherche(energie),safe=False)

def calcul(bd,choix,quantite):
    try:
        result_value = bd.calcul(choix,quantite)
        return JsonResponse(result_value,safe=False)
    except(ValueError):
        return JsonResponse({'message': f'{bd.name} invalide'},status = 404)