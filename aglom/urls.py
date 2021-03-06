from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
#from app_denuncias.views import ExampleView
from app_auth.api.viewsets import RegisterView, LoginView
from rest_framework import routers
from app_denuncias.api.viewsets import DenunciaViewSet

router = routers.DefaultRouter()
router.register(r'denuncia', DenunciaViewSet, basename='Denuncias')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    path('get-token/', obtain_jwt_token),
    path('sign-up/', RegisterView.as_view(), name='auth_register'),

    path('sign-in/', LoginView.as_view(), name='auth_login'),
]

'''
    rota protegida, teste
    path('example/', ExampleView.as_view()),
'''
