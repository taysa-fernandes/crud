#importação da biblioteca de filtros do django
import django_filters
#importação do modelo de filtros usado no projeto
from .models import Filtro,Pessoa
from django_filters import ModelChoiceFilter
#classe que permite definir filtros para campos especificos do modelo
class FiltroModelFilter(django_filters.FilterSet):
    # Define os filtros para cada campo do modelo
    nome = django_filters.CharFilter(lookup_expr='icontains')
    idade = django_filters.NumberFilter()
    email = django_filters.CharFilter(lookup_expr='icontains')
    telefone = django_filters.NumberFilter()
    created_at = django_filters.DateFilter()
    
    #classe que define os metadados do conjunto de filtros
    class Meta:
        model = Filtro # Define o modelo alvo dos filtros
        fields = ['nome','idade','email','telefone'] # Define os campos que serão utilizados como filtros
        
class PessoaModelFilter(django_filters.FilterSet):
    # Define os filtros para cada campo do modelo
    nome = django_filters.CharFilter(lookup_expr='icontains')
    idade = django_filters.NumberFilter()
    email = django_filters.CharFilter(lookup_expr='icontains')
    telefone = django_filters.NumberFilter()
    filtro = django_filters.ModelChoiceFilter(queryset=Filtro)

    
    #classe que define os metadados do conjunto de filtros
    class Meta:
        model = Pessoa # Define o modelo alvo dos filtros
        fields = ['nome','idade','email','telefone','filtro'] # Define os campos que serão utilizados como filtros