from django.db import models
from django.utils.translation import gettext_lazy

from cliente.models import Cliente


class Tipo(models.TextChoices):
    FELINO = 'FELINO', gettext_lazy('Felino')

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=6,
        choices=Tipo.choices,
        null=False,
    )
    peso = models.FloatField(max_length=3)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null = True, default = None)
