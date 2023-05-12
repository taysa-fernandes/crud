
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
