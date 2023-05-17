# Este trecho de código configura as URLs para um aplicativo Django.
# Ele define duas URLs principais: uma para a interface de administração do Django e outra para as URLs definidas no aplicativo "core".
from django.contrib import admin
from django.urls import path,include

from core import views 

# Define a lista de URLs vazia
urlpatterns = [
    # URL para a interface de administração do Django
    path('admin/', admin.site.urls),
    # URL vazia que mapeia para as URLs definidas no aplicativo "core"
    path('',include('core.urls')),
]
