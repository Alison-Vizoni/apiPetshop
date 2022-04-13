from django.db import models
from django.utils.translation import gettext_lazy

class Cidades(models.TextChoices):
    FLORIANÓPOLIS = 'FLORIANÓPOLIS', gettext_lazy('Florianópolis')
    CURITIBA = 'CURITIBA', gettext_lazy('Curitiba')
    SAO_PAULO = 'SAO_PAULO', gettext_lazy('São Paulo')
    RIO_DE_JANEIRO = 'RIO_DE_JANEIRO', gettext_lazy('Rio de Janeiro')

class Endereco(models.Model):
    logradouro = models.CharField(max_length=30)
    cep = models.IntegerField()
    numero = models.IntegerField()
    uf = models.CharField(max_length=30)
    cidade = models.CharField(
        max_length=20,
        choices=Cidades.choices,
        null=False,
    )
    complemento = models.CharField(max_length=20, null=True, blank=True)
