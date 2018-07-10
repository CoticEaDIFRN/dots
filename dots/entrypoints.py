from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from .models import Colaborador
from .serializers import ColaboradorSerializer


router = DefaultRouter()


class ColaboradorViewSet(ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

router.register(r'colaboradores', ColaboradorViewSet)
