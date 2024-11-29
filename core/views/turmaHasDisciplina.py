from rest_framework import viewsets
from core.models import TurmaHasDisciplina
from core.serializers import TurmaHasDisciplinaSerializer



class TurmaHasDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = TurmaHasDisciplina.objects.all()
    serializer_class = TurmaHasDisciplinaSerializer
