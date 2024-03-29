from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'patch']

