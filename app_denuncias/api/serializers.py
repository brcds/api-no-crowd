from rest_framework.serializers import ModelSerializer
from app_denuncias.models import Denuncias


class DenunciasSerializer(ModelSerializer):
    class Meta:
        model = Denuncias
        fields = ('id', 'id_user', 'logintude', 'latitude', 'nome_lugar',
                  'tipo_lugar', 'descricao', 'quantidade_pessoas', 'created_at',
                  'updated_at')
