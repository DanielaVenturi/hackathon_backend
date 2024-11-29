from rest_framework import viewsets
from core.models import Nota
from core.serializers import NotaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
