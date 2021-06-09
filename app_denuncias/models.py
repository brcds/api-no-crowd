from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from pytz import timezone


class Denuncias(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    logintude = models.FloatField()
    latitude = models.FloatField()
    nome_lugar = models.CharField(max_length=200)
    tipo_lugar = models.CharField(max_length=200)
    descricao = models.TextField()
    quantidade_pessoas = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nome_lugar


'''    data_hora_ocorrido = models.DateTimeField(
        datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M")) '''
