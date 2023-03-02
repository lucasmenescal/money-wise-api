from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics
from api.Models.pessoa import PessoaSerializer, Pessoa
from rest_framework import viewsets

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer