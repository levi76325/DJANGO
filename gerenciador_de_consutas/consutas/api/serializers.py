from rest_framework import serializers
from consutas.models import Consuta

class ConsutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consuta
        fields = '__all__' 