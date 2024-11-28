from rest_framework import serializers
from core.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '_all_'