from django.urls import path
from .views import cadastro, CadastroUsuarioView, ProdutosRecomendadosAPIView, LoginView, perfil_api
from . import views

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro_api'),
    path('recomendados/', ProdutosRecomendadosAPIView.as_view(), name='api-recomendados'),
    path('api/login/', LoginView.as_view(), name='loginAPI'),
    path('perfil/', perfil_api, name='api-perfil')
] 