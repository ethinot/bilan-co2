from rest_framework import routers, serializers, viewsets
from .models import User_data

class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_data
        fields = '__all__'