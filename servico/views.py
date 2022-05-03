from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from servico.models import Servico
from servico.serializers import ServicoSerializer


class ServicoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    http_method_names = ['get', 'post', 'patch']

