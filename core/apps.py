#importação da classe Appconfig que configura as aplicações django
from django.apps import AppConfig


#subclasse de de Appconfig para configurar as aplicações
class CoreConfig(AppConfig):
    # Define o tipo de campo automático padrão para as migrações
    default_auto_field = 'django.db.models.BigAutoField'
    # Define o nome da aplicação
    name = 'core'
