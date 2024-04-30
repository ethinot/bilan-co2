from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *
import pandas as pd

transport_bd = BD("transport.csv")
alimentation_bd = Alimentation("alimentation.csv")
energie_bd = BD("energie.csv")

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def User_data_view(request):
    """
    View function to retrieve user data or list all users.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: JSON response containing user data or list of users.
    """
    if request.method == 'GET':
        try:
            utilisateur = User_data.objects.get(user=request.user)
            serializer = UserDataSerializer(utilisateur, context={'request': request})
            return Response(serializer.data)
        except User_data.DoesNotExist:
            return Response({'message': 'Utilisateur non trouvé'}, status=404)
            
    return Response({'message': 'Méthode non autorisée'}, status=405)

@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def update_user_data(request):
    """
    View function to update user data.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: JSON response indicating success or failure of the update operation.
    """
    if request.method == 'PATCH':
        try:
            utilisateur = User_data.objects.get(user=request.user)
            data = request.data
            serializer = UserDataSerializer(utilisateur, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except User_data.DoesNotExist:
            return Response({'message': 'Utilisateur non trouvé'}, status=404)
            
    return Response({'message': 'Méthode non autorisée'}, status=405)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_consommation_by_user(request):
    """
    Retrieve all consommations for current user.

    Args:
        request: The request object.

    Returns:
        Response: The serialized data of all consommations for the user.

    Raises:
        HTTP_404_NOT_FOUND: If no consommations are found for the user.
    """
    try:
        consommations = Consommation.objects.filter(user=request.user)
        serializer = ConsommationSerializer(consommations, many=True, context={'request': request})
        return Response(serializer.data)
    except Consommation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_consommation_by_id(request, consommation_id):
    """
    Retrieve a specific consommation for a user by ID.

    Args:
        request: The request object.
         (int): The ID of the user.
        consommation_id (int): The ID of the consommation.

    Returns:
        Response: The serialized data of the consommation.

    Raises:
        HTTP_404_NOT_FOUND: If the consommation does not exist for the user.
    """
    try:
        consommation = Consommation.objects.get(user=request.user, id=consommation_id)
        serializer = ConsommationSerializer(consommation, context={'request': request})
        return Response(serializer.data)
    except Consommation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_consommation(request):
    """
    Create a new consommation for a specific user.

    Args:
        request: The request object.
         (int): The ID of the user.

    Returns:
        Response: The serialized data of the created consommation.

    Raises:
        HTTP_400_BAD_REQUEST: If the request data is invalid.
    """
    serializer = ConsommationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def update_consommation(request, consommation_id):
    """
    Update an existing consommation for a specific user.

    Args:
        request: The request object.
         (int): The ID of the user.
        consommation_id (int): The ID of the consommation.

    Returns:
        Response: The serialized data of the updated consommation.

    Raises:
        HTTP_404_NOT_FOUND: If the consommation does not exist for the user.
        HTTP_400_BAD_REQUEST: If the request data is invalid.
    """
    try:
        consommation = Consommation.objects.get(user=request.user, id=consommation_id)
    except Consommation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ConsommationSerializer(consommation, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_consommation(request, consommation_id):
    """
    Delete an existing consommation for a specific user.

    Args:
        request: The request object.
        consommation_id (int): The ID of the consommation.

    Returns:
        Response: Empty response with status code 204.

    Raises:
        HTTP_404_NOT_FOUND: If the consommation does not exist for the user.
    """
    try:
        consommation = Consommation.objects.get(user=request.user, id=consommation_id)
    except Consommation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    consommation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def calculateur_de_conso(request, type_calcul: str, choix: str, quantite: float):
    """
    Calculate consumption based on type, choice, and quantity.

    Args:
        request: The request object.
        type_calcul (str): The type of calculation.
        choix (str): The specified choice.
        quantite (float): The specified quantity.

    Returns:
        Response: The result of the calculation.

    Raises:
        HTTP_400_BAD_REQUEST: If the request data is invalid.
        HTTP_500_INTERNAL_SERVER_ERROR: If an error occurs during calculation.
    """
    try:
        if type_calcul == 'transport':
            resultat = transport_bd.calcul(choix, quantite)
        elif type_calcul == 'alimentation':
            resultat = alimentation_bd.calcul(choix, quantite)
        elif type_calcul == 'energie':
            resultat = energie_bd.calcul(choix, quantite)
        else:
            return Response({'error': 'Type de calcul non pris en charge.'}, status=400)
        
        return Response({'resultat': resultat})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def recherche_de_conso(request, categorie=None, sous_categorie=None, terme_recherche=None):
    """
    Search for consumption data.

    Args:
        request: The request object.
        categorie (str): The specified category.
        sous_categorie (str): The specified subcategory.
        terme_recherche (str): The specified search term.

    Returns:
        Response: The consumption data corresponding to the search parameters.

    Raises:
        HTTP_400_BAD_REQUEST: If the request data is invalid.
        HTTP_500_INTERNAL_SERVER_ERROR: If an error occurs during search.
    """
    try:
        if request.method == 'GET':
            if categorie == 'transport':
                if terme_recherche is None:
                    resultat = transport_bd.list_value()
                else:
                    resultat = transport_bd.recherche(terme_recherche)
            elif categorie == 'alimentation':
                if terme_recherche is None:
                    if sous_categorie is None:
                        resultat = alimentation_bd.list_value()
                    else:
                        resultat = alimentation_bd.select_sous_categorie(sous_categorie)
                else:
                    resultat = alimentation_bd.recherche(terme_recherche)
            elif categorie == 'energie':
                if terme_recherche is None:
                    resultat = energie_bd.list_value()
                else:
                    resultat = energie_bd.recherche(terme_recherche)
            else:
                return Response({'error': 'Type de recherche non pris en charge.'}, status=400)
            
            return Response(resultat)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
