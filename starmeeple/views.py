from django.shortcuts import render, redirect
from django.http import JsonResponse
from etabuleiros.services import criar_usuario, incluir_item_no_carrinho, atualizar_item_carrinho, incluir_item_desejos
from django.utils.timezone import localtime 
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from etabuleiros.models import Produto, Usuario, Categoria, Editora
from .serializers import ProdutoRecomendadoSerializer, UsuarioSerializer, LoginSerializer, CategoriaSerializer, ProdutoSerializer, PerfilSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.utils import timezone

class CriarCategoriaView(APIView):
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                categoria = serializer.save()
                return Response(
                    {
                        "success": "Categoria criada com sucesso",
                        "cat_id": categoria.cat_id,
                        "nome_categoria": categoria.nome_categoria
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        # Tratamento especial para erros de unicidade
        if 'nome_categoria' in serializer.errors and 'unique' in serializer.errors['nome_categoria'][0].code:
            return Response(
                {"error": "Esta categoria já existe."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CriarProdutoView(APIView):
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        
        if serializer.is_valid():
            # Processar os dados antes de salvar
            produto_data = serializer.validated_data
            
            # Verificar e obter categoria
            if 'cat' in produto_data:
                try:
                    categoria = Categoria.objects.get(id=produto_data['cat'].id)
                except Categoria.DoesNotExist:
                    return Response(
                        {"error": "Categoria não encontrada"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            # Verificar e obter editora
            if 'editora' in produto_data and produto_data['editora']:
                try:
                    editora = Editora.objects.get(id=produto_data['editora'].id)
                except Editora.DoesNotExist:
                    return Response(
                        {"error": "Editora não encontrada"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            # Adicionar data de criação
            produto_data['data_criacao'] = timezone.now()
            
            # Salvar o produto
            produto = Produtos.objects.create(**produto_data)
            
            return Response(
                {"success": "Produto criado com sucesso", "produto_id": produto.prod_id},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'HTML/home.html')

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
    return render(request, 'HTML/cateoriaJogosCartas.html')

def categoriaJogosTabuleiros(request):
    return render(request, 'HTML/cateoriaJogosTabuleiros.html')

def categoriaProibidao(request):
    return render(request, 'HTML/cateoriaProibidao.html')

def categoriaQuebraCabeca(request):
    return render(request, 'HTML/cateoriaQuebraCabeca.html')

def categoriaRPG(request):
    return render(request, 'HTML/cateoriaRPG.html')

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Verifica se o usuário está ativo
        if not user.is_active:
            return Response(
                {"detail": "Esta conta está inativa."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Gera tokens JWT
        refresh = RefreshToken.for_user(user)
        
        # Adiciona o user_id customizado ao token
        refresh['user_id'] = user.user_id
        
        return Response({
            "message": "Login realizado com sucesso",
            "user": {
                "user_id": user.user_id,  # Usando user_id em vez de id
                "email": user.email,
                "nome": user.nome,
                "tipo": user.tipo
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)

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
    return render(request, 'HTML/problemaPedido.html')

def produto(request):
    return render(request, 'HTML/produto.html')

def suporteCliente(request):
    return render(request, 'HTML/suporteCliente.html')

def suporteFuncionario(request):
    return render(request, 'HTML/suporteFuncionario.html')


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