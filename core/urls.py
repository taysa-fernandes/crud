from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDestroyView,PessoaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),
    path('pessoas/',PessoaListView.as_view(),name='pessoa'),
    path('pessoas/create/', PessoaCreateView.as_view(), name='pessoa-create'),
    path('pessoas/<int:pk>/update/', PessoaUpdateView.as_view(),name='pessoa-update'),
    path('pessoas/<int:pk>/delete/', PessoaDestroyView.as_view(),name='pessoa-delete'),

]
