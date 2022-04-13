from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from servico.serializers import ServicoSerializer
from cliente.models import Cliente


class ServicoViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ServicoSerializer
    http_method_names = ['get', 'post', 'patch']

