from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app_denuncias.models import Denuncias
from .serializers import DenunciasSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission


class DenunciaViewSet(viewsets.ModelViewSet):
    serializer_class = DenunciasSerializer

    def get_queryset(self):
        return Denuncias.objects.all()

    def create(self, request, *args, **kwargs):
        id_user = User.objects.filter(id=self.request.data['id_user']).first()
        denuncia = Denuncias.objects.create(
            id_user=id_user,
            logintude=self.request.data['logintude'],
            latitude=self.request.data['latitude'],
            nome_lugar=self.request.data['nome_lugar'],
            tipo_lugar=self.request.data['tipo_lugar'],
            descricao=self.request.data['descricao'],
            quantidade_pessoas=self.request.data['quantidade_pessoas']
        )

        denuncia.save()

        if status.HTTP_201_CREATED:
            return Response({"Denuncia realizada com sucesso"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Erro ao realizar denuncia"}, status=status.HTTP_400_BAD_REQUEST)
