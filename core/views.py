
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Pessoa,MyModel
from .serializers import PessoaSerializer,MyModelSerializer
from .filters import MyModelFilter

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MyModelFilter