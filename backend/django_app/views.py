from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from .serializers import *
from .models import *

# API views.

def User_data(request, id_user=None):

    if request.method == 'GET':
        print("request.method == 'GET'")

        if id_user is None: # if id_user is None. then its a request to get all users
            utilisateurs = User_data.objects.all()
            serializer = User_Data_Serializer(utilisateurs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                serializer = User_Data_Serializer(utilisateur)
                return JsonResponse(serializer.data)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    elif request.method == 'POST':
        print("request.method == 'POST'")
        # Assuming your request body contains JSON data with user information
        data = request.POST  # If data is JSON, you might use request.body instead
        
        # You need to deserialize and save data into the database
        serializer = User_Data_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)