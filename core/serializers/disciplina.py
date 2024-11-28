from rest_framework import serializers
from core.models import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '_all_'