from django.db import models
from rest_framework import serializers

class Pessoa(models.Model):
  class Meta:
    db_table = 'pessoa'

  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'