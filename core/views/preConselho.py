from rest_framework import viewsets
from core.models import PreConselho
from core.serializers import PreConselhoSerializer

class PreConselhoViewSet(viewsets.ModelViewSet):
    queryset = PreConselho.objects.all()
    serializer_class = PreConselhoSerializer