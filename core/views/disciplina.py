from rest_framework import viewsets
from core.models import Disciplina
from core.serializers import DisciplinaSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer