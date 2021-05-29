from rest_framework.viewsets import ModelViewSet
from app_denuncias.models import Denuncias
from .serializers import DenunciasSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission



class DenunciaViewSet(viewsets.ModelViewSet):

    queryset = Denuncias.objects.all()
    serializer_class = DenunciasSerializer
