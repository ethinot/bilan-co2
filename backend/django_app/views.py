from rest_framework.parsers import JSONParser, MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import *


@csrf_exempt
def User_data(request, id_user=None):

    if request.method == 'GET':
        if id_user is None:
            utilisateurs = User_data.objects.all()
            serializer = UserDataSerializer(utilisateurs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                serializer = UserDataSerializer(utilisateur)
                return JsonResponse(serializer.data)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    elif request.method == 'POST':
        data = request.POST.copy()
        serializer = UserDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        if id_user is not None:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                data = request.POST.copy()
                serializer = UserDataSerializer(utilisateur, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=400)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    elif request.method == 'PATCH':
        if id_user is not None:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                data = request.POST.copy()
                serializer = UserDataSerializer(utilisateur, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=400)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    elif request.method == 'DELETE':
        if id_user is not None:
            try:
                utilisateur = User_data.objects.get(user=id_user)
                utilisateur.delete()
                return HttpResponse(status=204)
            except User_data.DoesNotExist:
                return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)