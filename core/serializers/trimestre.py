from rest_framework import serializers
from core.models import Trimestre

class TrimestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trimestre
        fields = ['trimestre_id', 'nome', 'data_inicio', 'data_fim']
