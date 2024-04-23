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


def get_transport_list(request):
    if request.method == 'GET':
        return JsonResponse(tr.transport_list(),safe=False)

def recherche_transport(request,transport:str):
    if request.method == 'GET':
        return JsonResponse(tr.recherche(transport),safe=False)

def calcul(bd,choix,quantite):
    try:
        result_value = bd.calcul(choix,quantite)
        return JsonResponse(result_value,safe=False)
    except(ValueError):
        return JsonResponse({'message': f'{bd.name} invalide'},status = 404)