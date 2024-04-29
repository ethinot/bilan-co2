from rest_framework import routers, serializers, viewsets
from .models import *

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method == 'PATCH':
            for field_name, field in self.fields.items():
                field.required = False

class ConsommationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method == 'PATCH':
            for field_name, field in self.fields.items():
                field.required = False

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method == 'PATCH':
            for field_name, field in self.fields.items():
                field.required = False
