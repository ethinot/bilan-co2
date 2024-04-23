from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from django_app.models import User

class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'champ_1')
