from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *

# API views.

def User_data(request, id_user=None):

    if request.method == 'GET':
        print("request.method == 'GET'")

        if id_user is None: # if id_user is None. then its a request to get all users
            utilisateurs = User_data.objects.all()
            serializer = UtilisateurSerializer(utilisateurs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                serializer = UtilisateurSerializer(utilisateur)
                return JsonResponse(serializer.data)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    elif request.method == 'POST':
        print("request.method == 'POST'")
    elif request.method == 'PUT':
        print("request.method == 'PUT'")
    elif request.method == 'PATCH':
        print("request.method == 'PATCH'")
    elif request.method == 'DELETE':
        print("request.method == 'DELETE'")