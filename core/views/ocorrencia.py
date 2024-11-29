from rest_framework import viewsets
from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer

class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
