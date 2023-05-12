from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import PessoaViewSet

router = DefaultRouter()
router.register(r'pessoa', PessoaViewSet, basename='pessoa')

urlpatterns = [
   
] + router.urls
