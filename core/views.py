
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    #filtra de acordo com uma idade mínima e máxima
    def get_queryset(self):
        queryset = Pessoa.objects.all()
        idade_min = self.request.query_params.get('idade_min', None)
        idade_max = self.request.query_params.get('idade_max', None)
        inicial_nome = self.request.query_params.get('inicial_nome', None)
        telefone = self.request.query_params.get('telefone', None)
        email = self.request.query_params.get('email', None)
        
        if idade_min is not None:
            queryset = queryset.filter(idade__gte=idade_min)
        if idade_max is not None:
            queryset = queryset.filter(idade__lte=idade_max)
        if idade_min is not None and idade_max is not None:
            queryset = queryset.filter(idade__range=(idade_min, idade_max))
        if inicial_nome is not None:
            queryset = queryset.filter(nome__istartswith=inicial_nome)
        if telefone is not None:
            queryset = queryset.filter(telefone=telefone)
        if email is not None:
            queryset = queryset.filter(email=email)

        return queryset