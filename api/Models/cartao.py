from django.db import models
from rest_framework import serializers
from .tipo_cartao import Tipo_Cartao
# Create your models here.

class Cartao(models.Model):
  class Meta:
    db_table = 'cartao'

  nome = models.CharField(max_length=100)
  tipo_cartao = models.ForeignKey('Tipo_Cartao', on_delete=models.CASCADE)






class CartaoSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cartao
      fields = '__all__'