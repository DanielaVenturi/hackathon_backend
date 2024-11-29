from core.models.ocorrencia import Ocorrencia
from rest_framework import serializers
from core.models import Ocorrencia

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '_all_'
