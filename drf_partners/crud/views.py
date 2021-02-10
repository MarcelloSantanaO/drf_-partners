from rest_framework import viewsets
from .serializers import PartnerSerializer
from .models import Partner


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('name')
    serializer_class = PartnerSerializer