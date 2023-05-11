from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDestroyView,PessoaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),
    path('pessoas/',PessoaListView.as_view()),
    path('pessoas/create/', PessoaCreateView.as_view()),
    path('pessoas/<int:pk>/update/', PessoaUpdateView.as_view()),
    path('pessoas/<int:pk>/delete/', PessoaDestroyView.as_view()),

]
