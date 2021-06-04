import calendar
import datetime
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app_denuncias.models import Denuncias
from .serializers import DenunciasSerializer
from rest_framework import viewsets, status


class DenunciaViewSet(viewsets.ModelViewSet):
    serializer_class = DenunciasSerializer

    def get_queryset(self):
        start_date = timezone.now().date()
        end_date_today = start_date + timedelta(days=1)

        srtday = int(calendar.monthrange(2021, 5)[1]) + int(start_date.strftime("%d"))
        endday = int(calendar.monthrange(2021, 5)[1]) - int(start_date.strftime("%d"))

        start_date_week = start_date + timedelta(days=+1)
        end_date_week = start_date + timedelta(days=-8)

        start_date_month = start_date + timedelta(days=-srtday)
        end_date_month = start_date + timedelta(days=+endday)

        search = self.request.query_params.get('search', None)
        queryset = Denuncias.objects.all()

        if search == 'today':
            queryset = queryset.filter(created_at__range=(start_date, end_date_today))
            return queryset
        if search == 'week':
            queryset = queryset.filter(created_at__range=(end_date_week, start_date_week))
            return queryset
        if search == 'month':
            queryset = queryset.filter(created_at__range=(start_date_month, end_date_month))
            return queryset

        return queryset

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
