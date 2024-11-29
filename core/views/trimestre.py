from rest_framework import viewsets
from core.models import Trimestre
from core.serializers import TrimestreSerializer


class TrimestreViewSet(viewsets.ModelViewSet):
    queryset = Trimestre.objects.all()
    serializer_class = TrimestreSerializer