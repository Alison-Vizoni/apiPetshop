from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from endereco.serializers import EnderecoSerializer
from cliente.models import Cliente


class EnderecoViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'patch']

