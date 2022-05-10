from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from cliente.serializers import ClienteSerializer
from cliente.models import Cliente


class ClienteViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'patch']

