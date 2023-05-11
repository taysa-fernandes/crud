from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDestroyView,PessoaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),
    path('pessoas/',PessoaListView.as_view()),
    path('pessoas/create/', PessoaCreateView.as_view()),
    path('pessoas/<int:pk>/update/', PessoaUpdateView.as_view()),
    path('pessoas/<int:pk>/delete/', PessoaDestroyView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='API Docs')),
]
