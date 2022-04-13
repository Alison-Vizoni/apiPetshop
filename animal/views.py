from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from animal.models import Animal
from animal.serializers import AnimalSerializers


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializers
    http_method_names = ['get', 'post', 'patch']
