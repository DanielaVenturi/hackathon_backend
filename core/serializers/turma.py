from rest_framework import serializers
from core.models import Turma

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '_all_'
