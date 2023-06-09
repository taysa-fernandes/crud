
# Este trecho de código define classes de visualização para um aplicativo Django usando o Django REST Framework.
# Ele define uma classe de visualização chamada PessoaViewSet, que manipula operações CRUD para o modelo Pessoa.
# Também define uma classe de visualização chamada MyModelList, que lista e cria instâncias do modelo MyModel.
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters import rest_framework as rf
from .models import Pessoa,Filtro
from .serializers import PessoaSerializer,FiltroSerializer
from .filters import FiltroModelFilter,PessoaModelFilter

#Classe de visualização para manipular operações CRUD no modelo Pessoa
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filterset_class = PessoaModelFilter
    filter_backends = [filters.SearchFilter,rf.DjangoFilterBackend]
    search_fields = ['nome', 'idade', 'email', 'telefone']

#Classe de visualização para listar e criar instâncias do modelo Filtro
class FiltroList(generics.ListCreateAPIView):
    queryset = Filtro.objects.all()
    serializer_class = FiltroSerializer
    filterset_class = FiltroModelFilter