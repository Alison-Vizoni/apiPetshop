from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['get', 'post', 'patch']

