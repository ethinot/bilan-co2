from rest_framework import routers, serializers, viewsets
from .models import User_data

class User_Data_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User_data
        fields = '__all__'