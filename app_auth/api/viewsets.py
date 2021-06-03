from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from app_auth.api.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)

        if status.HTTP_200_OK:
            return Response({
                'Usuário Cadastrado': True,
                'username': response.data['username'],
                'token': token
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({f"Usuário Cadastrado': {False},Erro ao cadastrar Usuario"},
                            status=status.HTTP_400_BAD_REQUEST)
