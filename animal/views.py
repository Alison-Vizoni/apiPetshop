from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from animal.models import Animal
from animal.serializers import AnimalSerializers


class AnimalViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializers
    http_method_names = ['get', 'post', 'patch']
