from django.db import models
from django.utils.translation import gettext_lazy


class Turno(models.TextChoices):
    MATUTINO = 'MATUTINO', gettext_lazy('Matutino')
    VESPERTINO = 'VESPERTINO', gettext_lazy('Vespertino')
    NOTURNO = 'NOTURNO', gettext_lazy('Noturno')

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20)
    turno = models.CharField(
        max_length=10,
        choices=Turno.choices,
        null=False,
    )
