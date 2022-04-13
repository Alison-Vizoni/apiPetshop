"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from animal.views import AnimalViewSet
from cliente.views import ClienteViewSet
from endereco.views import EnderecoViewSet
from funcionario.views import FuncionarioViewSet
from servico.views import ServicoViewSet

router = routers.SimpleRouter()
router.register("cliente", ClienteViewSet)
router.register("animal", AnimalViewSet)
router.register("endereco", EnderecoViewSet)
router.register("funcionario", FuncionarioViewSet)
router.register("servico", ServicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
