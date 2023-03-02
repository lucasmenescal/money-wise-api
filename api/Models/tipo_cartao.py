from django.db import models

# Create your model here.

class Tipo_Cartao(models.Model):
  class Meta:
    db_table = 'tipo_cartao'

  nome = models.CharField(max_length=100)