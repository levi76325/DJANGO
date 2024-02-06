from rest_framework import viewsets
from .serializers import ConsutaSerializer
from consutas.models import Consuta

class ConsutaViewSet(viewsets.ModelViewSet):
    queryset = Consuta.objects.all()
    serializer_class = ConsutaSerializer  