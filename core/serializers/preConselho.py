from core.models.preConselho import PreConselho
from rest_framework import serializers
from core.models import PreConselho

class PreConselhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreConselho
        fields = '_all_'