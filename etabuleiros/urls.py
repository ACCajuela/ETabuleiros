"""
URL configuration for etabuleiros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from starmeeple import views
from django.urls import path
from starmeeple.views import ProdutosRecomendadosAPIView, CadastroUsuarioView, LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('adm/editClient', views.editCliente, name='editClient'),
    path('adm/editEmployee', views.editFuncionarioAdm, name='editEmployee'),
    path('login', views.login, name='/login'),
    path('pay', views.pedido, name='pedido'),
    path('cart', views.carrinho, name='carrinho'),
    path('cat/cards', views.categoriaJogosCartas, name='categoriaCartas'),
    path('cat/boardgames', views.categoriaJogosTabuleiros, name='categoriaTabuleiro'),
    path('cat/prohib', views.categoriaProibidao, name='categoriaAdulto'),
    path('cat/puzzle', views.categoriaQuebraCabeca, name='categoriaQuebraCabeva'),
    path('cat/rpg', views.categoriaRPG, name='RPG'),
    path('adm/finance', views.exportaFinanca, name='exportarFinanca'),
    path('wish', views.listaDesejos, name='listaDesejos'),
    path('adm/panel', views.painelADM, name='painelAdm'),
    path('profile', views.perfil, name='perfil'),
    path('pay/issue', views.problemaPedido, name='problemaPedido'),
    path('product', views.produto, name='produto'),
    path('custSuport', views.suporteCliente, name='suporteCliente'),
    path('adm/custSuport', views.suporteFuncionario, name='suporteFuncionario'),
    path('api/recomendados/', ProdutosRecomendadosAPIView.as_view(), name='api-recomendados'),
    path('api/cadastro/', CadastroUsuarioView.as_view(), name='cadastro-usuario'),
    path('api/login/', LoginView.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)