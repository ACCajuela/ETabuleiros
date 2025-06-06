from django.shortcuts import render, redirect
from django.http import JsonResponse
from etabuleiros.services import criar_usuario, incluir_item_no_carrinho, atualizar_item_carrinho, incluir_item_desejos
from django.utils.timezone import localtime 
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from etabuleiros.models import Produto, Usuario, Categoria, Editora
from .serializers import ProdutoRecomendadoSerializer, UsuarioSerializer, LoginSerializer, PerfilSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.utils.decorators import method_decorator 
from django.views.generic import View
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from .models import Produto
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from django.shortcuts import render, redirect
from etabuleiros.forms import ProdutoForm  # Importe o formulário

@csrf_exempt
def criar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome = data.get('nome_categoria', '').strip()

            if not nome:
                return JsonResponse({'status': 'error', 'message': 'Nome da categoria é obrigatório'}, status=400)

            # Tenta criar a nova categoria
            categoria = Categoria(nome_categoria=nome)
            categoria.save()

            return JsonResponse({'status': 'success', 'message': f'Categoria \"{nome}\" criada com sucesso!'})
        
        except IntegrityError:
            return JsonResponse({'status': 'error', 'message': 'Esta categoria já existe.'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Erro interno: {str(e)}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


def home(request):
    return render(request, 'HTML/home.html')

def editProdutoCategoria(request):
    return render(request, 'HTML/editProdutoCategoria.html')

def adicionar_produto(request):
    print('entrou')
    if request.method == 'GET':
        return JsonResponse({}, status=200)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redireciona após salvar
    else:
        form = ProdutoForm()
    
    return render(request, 'adicionar_produto.html', {'form': form})




def cadastro(request):
    return render(request, 'HTML/cadastro.html')

class CadastroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Usuário criado com sucesso!"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

def carrinho(request):
    return render(request, 'HTML/carrinho.html')

def categoriaJogosCartas(request):
    return render(request, 'HTML/categoriaJogosCartas.html')

def categoriaJogosTabuleiros(request):
    return render(request, 'HTML/categoriaJogosTabuleiros.html')

def categoriaProibidao(request):
    return render(request, 'HTML/categoriaProibidao.html')

def categoriaQuebraCabeca(request):
    return render(request, 'HTML/categoriaQuebraCabeca.html')

def categoriaRPG(request):
    return render(request, 'HTML/categoriaRPG.html')

def editCliente(request):
    return render(request, 'HTML/editCliente.html')

def editFuncionarioAdm(request):
    return render(request, 'HTML/editFuncionarioAdm.html')

def exportaFinanca (request):
    return render(request, 'HTML/exportaFinanca.html')

def listaDesejos (request):
    return render(request, 'HTML/listaDesejos.html')

def login(request):
    return render(request, 'HTML/login.html')

User = get_user_model()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            if not user.is_active:
                return Response(
                    {"detail": "Conta inativa. Contate o administrador."},
                    status=status.HTTP_403_FORBIDDEN
                )

            refresh = RefreshToken.for_user(user)
            refresh['user_id'] = user.user_id  # Custom claim

            return Response({
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                "user": {
                    "user_id": user.user_id,
                    "email": user.email,
                    "nome": user.nome or user.email.split('@')[0],  # Fallback
                    "tipo": user.tipo
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

def painelADM(request):
    return render(request, 'HTML/painelADM.html')

def pedido(request):
    return render(request, 'HTML/pedido.html')

def perfil(request):
    return render(request, 'HTML/perfil.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_api(request):
    serializer = PerfilSerializer(request.user)
    return Response(serializer.data)

def problemaPedido(request):
    return render(request, 'templates/HTML/problemaPedido.html')

def produto(request):
    return render(request, 'templates/HTML/produto.html')

def suporteCliente(request):
    return render(request, 'templates/HTML/suporteCliente.html')

def suporteFuncionario(request):
    return render(request, 'templates/HTML/suporteFuncionario.html')

def categoriaFamilia(request):
    return render(request, 'templates/HTML/categoriaFamilia.html')


def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = criar_usuario(nome, email, senha)
            return JsonResponse({'id': usuario.id, 'nome': usuario.first_name})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
        
def editar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')  
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')  

        try:
            usuario = editar_usuario(user_id, nome, email, senha)
            return JsonResponse({'status': 'ok', 'usuario': usuario.first_name})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)

'''
def desativar_usuario(request):
    if request.method == 'POST':
        user_id = request.user.id 

        try:
            desativar_usuario(user_id)
            return JsonResponse({'status': 'Conta desativada com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
'''


'''  


def fazer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            user = fazer_login(request, email, senha)
            return redirect('home')
        except ValueError as e:
            return render(request, 'login', {'erro': str(e)})
    return render(request, 'login')

def fazer_logout(request):
    fazer_logout(request)
    return redirect('home')


'''
def desativar_usuario(request):
    if request.method == 'POST':
        user_id = request.user.id 
        try:
            desativar_usuario(user_id)
            return JsonResponse({'status': 'Conta desativada com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
        
'''

def incluir_carrinho(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        try:
            carrinho = incluir_item_no_carrinho(email, produto_id, quantidade)
            return JsonResponse({
                'id': carrinho.id,
                'produto': carrinho.produto.id,
                'usuario': carrinho.usuario.id,
                'quantidade': carrinho.quantidade,
                'data_inclusao': localtime(carrinho.data_inclusao).strftime('%d/%m/%Y %H:%M')
            })
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
        
def editar_carrinho(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        produto_id = request.POST.get('produto')
        nova_quantidade = request.POST.get('quantidade')
        try:
            carrinho = atualizar_item_carrinho(email, produto_id, nova_quantidade)
            return JsonResponse({
                'id': carrinho.id,
                'produto': carrinho.produto.id,
                'usuario': carrinho.usuario.id,
                'quantidade': carrinho.quantidade,
                'data_atualizacao': localtime(carrinho.data_inclusao).strftime('%d/%m/%Y %H:%M')
            })
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
'''
def excluir_do_carrinho(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        produto_id = request.POST.get('produto')
        try:
            remover_item_carrinho(email, produto_id)
            return JsonResponse({'mensagem': 'Produto removido do carrinho com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
'''      

'''    

def incluir_desejos(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        produto_id = request.POST.get('produto')
        try:
            desejos = incluir_item_desejos(email, produto_id)
            return JsonResponse({
                'id': desejos.id,
                'produto': desejos.produto.id,
                'usuario': desejos.usuario.id,
                'data_inclusao': localtime(desejos.data_inclusao).strftime('%d/%m/%Y %H:%M')
            })
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
'''
def excluir_desejos(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        produto_id = request.POST.get('produto')
        try:
            remover_item_desejos(email, produto_id)
            return JsonResponse({'mensagem': 'Produto removido do carrinho com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)
'''
class ProdutosRecomendadosAPIView(generics.ListAPIView):
    """
    API para listar produtos marcados como recomendados
    """
    serializer_class = ProdutoRecomendadoSerializer
    
    def get_queryset(self):
        queryset = Produto.objects.filter(
            recomendado=True, 
        ).order_by('-data_criacao')[:12]  # Limita a 12 produtos mais recentes
        
        # Filtro opcional por categoria via query parameter
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria__slug=categoria)
            
        return queryset

'''
User = get_user_model()

class UserDetailAPIView():
    def get(self, request, pk):
        try:
            user = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)
'''