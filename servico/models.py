from django.db import models

from animal.models import Animal
from cliente.models import Cliente
from funcionario.models import Funcionario


class Servico(models.Model):
    Data = models.DateField()
    animal = models.ForeignKey(Animal, models.DO_NOTHING, null = True, default = None)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null = True, default = None)
    valor = models.FloatField(max_length=4)
    descricao = models.CharField(max_length=255)
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, null = True, default = None)
