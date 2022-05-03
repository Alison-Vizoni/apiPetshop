from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer


class FuncionarioViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['get', 'post', 'patch']

