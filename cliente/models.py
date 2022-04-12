from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, null = True, default = None)
    telefone = models.CharField(max_length=11)
