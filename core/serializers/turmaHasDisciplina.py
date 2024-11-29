from rest_framework import serializers
from core.models import TurmaHasDisciplina


class TurmaHasDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurmaHasDisciplina
        fields = '_all_'
