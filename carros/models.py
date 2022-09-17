from django.db import models


class Carros(models.Model):

    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    comentario = models.CharField(max_length=128)

