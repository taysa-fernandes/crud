#importação do módulo que define os modelos de dados mapeados do banco de dados
from django.db import models

#define o modelo Filtro
class Filtro(models.Model):
    #definição dos capos do modelo
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    #método que retorna uma representação legível para o objeto Filtro
    def __str__(self):
        return self.nome

#define o modelo pessoa
class Pessoa(models.Model):
    #definição dos campos do modelo
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    filtro = models.ForeignKey(Filtro,on_delete=models.CASCADE,default=1)
    #método que retorna uma representação legível para o objeto Pessoa
    def __str__(self):
        return self.nome
