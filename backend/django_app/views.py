from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *

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
            serializer = UserDataSerializer(utilisateur)
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
            serializer = UserDataSerializer(utilisateur, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except User_data.DoesNotExist:
            return Response({'message': 'Utilisateur non trouvé'}, status=404)
            
    return Response({'message': 'Méthode non autorisée'}, status=405)

@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_user_data(request):
    """
    View to delete user data.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: HTTP response indicating success or failure of the delete operation.
    """
    if request.method == 'DELETE':
        try:
            utilisateur = User_data.objects.get(user=request.user)
            utilisateur.delete()
            return Response(status=204)
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
        serializer = ConsommationSerializer(consommations, many=True)
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
        serializer = ConsommationSerializer(consommation)
        return Response(serializer.data)
    except Consommation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_consommation(request, ):
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
    serializer = ConsommationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['PUT'])
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

    serializer = ConsommationSerializer(consommation, data=request.data)
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
