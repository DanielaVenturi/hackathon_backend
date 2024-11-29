from rest_framework import serializers
from core.models import Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '_all_'
