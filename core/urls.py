# Este trecho de código configura as URLs para um aplicativo Django que usa o Django REST Framework.
# Ele define uma rota para a visualização "PessoaViewSet" e inclui todas as URLs geradas automaticamente no aplicativo.
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import PessoaViewSet

# Cria uma instância do DefaultRouter
router = DefaultRouter()
# Registra a visualização PessoaViewSet com a rota 'pessoa'
router.register(r'pessoa', PessoaViewSet, basename='pessoa')

# Define a lista de URLs  e concatena as rotas automaticas do default router
urlpatterns = [
   # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + router.urls
