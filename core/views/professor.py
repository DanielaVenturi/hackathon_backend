from rest_framework import viewsets
from core.models import Professor
from core.serializers import ProfessorSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer