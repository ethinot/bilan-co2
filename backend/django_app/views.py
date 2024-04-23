# views.py
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django_app.models import Transport

tr= Transport()

def get_te(_):
    

    result_value = tr.calcul("ter",100)

    html_content = f"<p>Résultat trouvé : {result_value}</p>"

    # Return HTML response
    return HttpResponse(html_content)
def calcul_transport(_,transport:str,km:float):
    try:
        result_value = tr.calcul(transport,km)
        return JsonResponse(result_value,safe=False)
    except(ValueError):
        return JsonResponse({'message': 'Transport invalide'},status = 404)


def get_transport_list(_):
    return JsonResponse(tr.transport_list(),safe=False)

def recherche_transport(_,transport:str):
    return JsonResponse([i for i in tr.transport_list() if transport.lower() in i.lower()],safe=False)