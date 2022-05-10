from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet

from animal.models import Animal
from animal.serializers import AnimalSerializers
from cliente.serializers import ClienteSerializer


class AnimalViewSet(ModelViewSet):
    permission_classes = (DjangoObjectPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializers
    http_method_names = ['get', 'post', 'patch']

    def retrive(self, request, *args, **kwargs):
        self.serializer_class = ClienteSerializer
        return super().retrive(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = ClienteSerializer
        return super().list(request, *args, **kwargs)