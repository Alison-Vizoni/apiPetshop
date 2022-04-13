from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from funcionario.serializers import FuncionarioSerializer
from cliente.models import Cliente


class FuncionarioViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['get', 'post', 'patch']

