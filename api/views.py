from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import Pessoa
from rest_framework import generics
from .serializers import PessoaSerializer
from rest_framework import viewsets

# Create your views here.

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer