from rest_framework import viewsets
from core.models import Turma
from core.serializers import TurmaSerializer



class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer