from django.db import models

class Tipo_Cartao(models.Model):
  class Meta:
    db_table = 'tipo_cartao'

  nome = models.CharField(max_length=100)