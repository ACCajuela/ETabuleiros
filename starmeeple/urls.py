from django.urls import path
from .views import cadastro, CadastroUsuarioView, ProdutosRecomendadosAPIView, LoginView, perfil_api
from . import views

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro_api'),
    path('recomendados/', ProdutosRecomendadosAPIView.as_view(), name='api-recomendados'),
    path('login/', LoginView.as_view(), name='login'),
    path('perfil/', perfil_api, name='api-perfil'),
]