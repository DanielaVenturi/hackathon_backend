from rest_framework import serializers
from core.models import ConselhoClasse

class ConselhoClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConselhoClasse
        fields = '_all_'
