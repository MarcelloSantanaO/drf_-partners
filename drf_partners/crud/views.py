from rest_framework import viewsets
from .serializers import PartnerSerializer
from .models import Partner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('name')
    serializer_class = PartnerSerializer

class PartnerApi(APIView):
    def post(self, request, format= None):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            rqst = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{serializer.validated_data['cnpj']}")
            result = json.loads(rqst.content)
            if result:
                serializer.validated_data['name'] = result['nome']
                serializer.validated_data['uf'] = result['uf']
                serializer.validated_data['phone'] = result['telefone']
                serializer.validated_data['email'] = result['email']
                serializer.validated_data['cnpj_status'] = result['situacao']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)