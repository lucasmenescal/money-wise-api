from django.db import models

# Create your models here.

class Pessoa(models.Model):
  class Meta:
    db_table = 'pessoa'

  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()