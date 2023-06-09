#importação da classe que converte objetos python em formatos json
from rest_framework import serializers
#improtação dos modelos usados no projeto
from .models import Pessoa, Filtro

#classe que serializa o modelo Pessoa
class PessoaSerializer(serializers.ModelSerializer):
    #Classe que configura o serializador
    class Meta:
        model = Pessoa #especifica que o modelo Pessoa que será serializado
        fields = ['id', 'nome', 'idade', 'email', 'telefone', 'parceiro'] #indica  os campos que será serializado
    #Método que cria a nova instância de Pessoa
    def create(self, validated_data):
        return Pessoa.objects.create(**validated_data)

#Classe que serializa o modelo Filtro
class FiltroSerializer(serializers.ModelSerializer):
    #Classe que configura o serializador
    class Meta:
        model = Filtro #especifica que o modelo Filtro que será serializado
        fields = ['id', 'nome', 'idade', 'email', 'telefone'] #indica que os campos id,nome,idade,email e telefone será serializado