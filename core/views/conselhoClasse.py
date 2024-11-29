from rest_framework import viewsets
from core.models import ConselhoClasse
from core.serializers import ConselhoClasseSerializer


class ConselhoClasseViewSet(viewsets.ModelViewSet):
    queryset = ConselhoClasse.objects.all()
    serializer_class = ConselhoClasseSerializer