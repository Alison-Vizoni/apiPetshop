from tokenize import Token

from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import UserModel
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch']


class UserAuthView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        if request.data.get("username") is None or request.data.get("password") is None:
            return Response({"message": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserModel.objects.filter(username=request.data.get("username")).first()

        if user is None:
            return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        if user.password == request.data.get("password"):
            user.set_password(user.password)
            user.save()

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": user.username,
            "token": token.key,
        })
