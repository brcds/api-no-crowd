from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from app_denuncias.views import ExampleView
from app_auth.api.viewsets import RegisterView
from rest_framework import routers
from app_denuncias.api.viewsets import DenunciaViewSet

router = routers.DefaultRouter()
router.register(r'denuncia', DenunciaViewSet, basename='Denuncias')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('token/', obtain_jwt_token),

    path('example/', ExampleView.as_view()),

    path('sign-up/', RegisterView.as_view(), name='auth_register'),

]
