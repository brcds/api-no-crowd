from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from app_auth.api.serializers import RegisterSerializer
from app_denuncias.models import Denuncias


class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = User.objects.get(username=response.data['username'])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        if status.HTTP_200_OK:
            return Response({
                'id': user.id,
                'first_name': user.first_name,
                'email': user.email,
                'username': response.data['username'],
                'token': token
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({f"Erro ao cadastrar Usuario"},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        # response = super().create(request, *args, **kwargs)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = User.objects.get(username=request.data['username'])

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        if user.check_password(request.data['password']):
            return Response({
                'id': user.id,
                'first_name': user.first_name,
                'email': user.email,
                'username': request.data['username'],
                'token': token
            }, status=status.HTTP_200_OK)
        else:
            return Response({f"Erro de login"},
                            status=status.HTTP_400_BAD_REQUEST)
