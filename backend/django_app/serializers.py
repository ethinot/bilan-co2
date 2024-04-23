from rest_framework import routers, serializers, viewsets
from .models import *

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_data
        fields = '__all__'