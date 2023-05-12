
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaListView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaCreateView(generics.CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [AllowAny] 

class PessoaUpdateView(generics.UpdateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [AllowAny] 

class PessoaDestroyView(generics.DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [AllowAny] 