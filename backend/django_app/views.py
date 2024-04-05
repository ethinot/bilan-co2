# views.py
import pandas as pd
from django.http import HttpResponse
from django_app.models import Transport

def get_te(_):
    transport= Transport()

    result_value = transport.calcul("ter",100)

    html_content = f"<p>Résultat trouvé : {result_value}</p>"

    # Return HTML response
    return HttpResponse(html_content)
