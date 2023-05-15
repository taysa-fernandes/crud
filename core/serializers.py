from rest_framework import serializers
from .models import Pessoa, MyModel
import django_filters
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
    def create(self, validated_data):
        return Pessoa.objects.create(**validated_data)

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'nome', 'idade', 'email', 'telefone', 'created_at']