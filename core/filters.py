import django_filters
from .models import MyModel

class MyModelFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    idade = django_filters.NumberFilter()
    email = django_filters.CharFilter(lookup_expr='icontains')
    telefone = django_filters.NumberFilter()
    created_at = django_filters.DateFilter()
    class Meta:
        model = MyModel
        fields = ['nome','idade','email','telefone','created_at']