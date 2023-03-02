from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from api.Models.cartao import CartaoSerializer
from api.Models.cartao import Cartao

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer