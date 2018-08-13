from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import Colaborador


class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('cpf', 'nome')
