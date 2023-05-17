#importação para acessar o painel de administração
from django.contrib import admin
#importaçao do modelo pessoa usado no projeto
from .models import Pessoa,Filtro

#classe que permite personalizar a exibição e comportamento do django admin de Pessoa
class PessoaAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na listagem
    list_display = ('nome', 'email', 'telefone')
# Registra o modelo "Pessoa" no Django Admin usando a classe "PessoaAdmin"
admin.site.register(Pessoa, PessoaAdmin)

#classe que permite personalizar a exibição e comportamento do django admin de Filtro
class FiltroAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na listagem
    list_display =('nome','email','telefone')
    
admin.site.register(Filtro,FiltroAdmin)
