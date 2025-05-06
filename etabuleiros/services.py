from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
from django.core.exceptions import ValidationError
from django.utils import timezone

'''def get_usuario_por_email(email):
    try:
        return Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')

def get_produto_por_id(produto_id):
    try:
        return Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
'''

def criar_usuario(nome, email, senha):
    if User.objects.filter(email=email).exists():
        raise ValueError("Email já cadastrado")
    usuario = User.objects.create_user(
        username=email,
        email=email,
        password=senha,
        first_name=nome
    )
    return usuario

def editar_usuario (id_usuario, nome=None, email=None, senha=None):
    try:
        usuario = User.objects.get(id=id_usuario)
    except User.DoesNotExist:
        raise ValueError("Usuário não encontrado")

    if nome:
        usuario.first_name = nome
    if email:
        usuario.email = email
        usuario.username = email 
    if senha:
        usuario.set_password(senha)
    usuario.save()
    return usuario

def fazer_logout(request):
    logout(request)

def fazer_login (request,email,senha):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("Email não cadastrado")
    
    user = authenticate(request, username=user.email, password=senha)
    
    if user is not None:
        django_login(request, user)
        return user
    else:
        raise ValidationError("Senha incorreta")
        
    
def desativar_usuario(id_usuario):
    try:
        usuario = User.objects.get(id=id_usuario)
        usuario.is_active = False
        usuario.save()
        return True
    except User.DoesNotExist:
        raise ValueError("Usuário não encontrado")
    
def incluir_item_no_carrinho(email, produto_id, quantidade):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        produto = produto.objects.get(id=produto_id)
    except produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    try:
        quantidade = int(quantidade)
    except ValueError:
        raise ValueError('Quantidade inválida')
    carrinho = carrinho.objects.create(
        usuario=usuario,
        produto=produto,
        quantidade=quantidade,
        data=timezone.now()  
    )
    return carrinho

def atualizar_item_carrinho(email, produto_id, nova_quantidade):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        produto = produto.objects.get(id=produto_id)
    except produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    try:
        nova_quantidade = int(nova_quantidade)
        if nova_quantidade <= 0:
            raise ValueError('A quantidade deve ser maior que zero')
    except ValueError:
        raise ValueError('Quantidade inválida')
    try:
        carrinho = carrinho.objects.get(usuario=usuario, produto=produto)
        carrinho.quantidade = nova_quantidade
        carrinho.save()
    except carrinho.DoesNotExist:
        raise ValueError('Produto não encontrado no carrinho')
    return carrinho


def remover_item_carrinho(email, produto_id):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        produto = produto.objects.get(id=produto_id)
    except produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    try:
        carrinho = carrinho.objects.get(usuario=usuario, produto=produto)
        carrinho.delete()
    except carrinho.DoesNotExist:
        raise ValueError('Produto não está no carrinho')
    
    return True

def incluir_item_desejos(email, produto_id):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        produto = produto.objects.get(id=produto_id)
    except produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    desejos = desejos.objects.create(
        usuario=usuario,
        produto=produto,
        data=timezone.now()  
    )

    return desejos

def remover_item_desejos(email, produto_id):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        produto = produto.objects.get(id=produto_id)
    except produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    try:
        desejos= desejos.objects.get(usuario=usuario, produto=produto)
        desejos.delete()
    except desejos.DoesNotExist:
        raise ValueError('Produto não está no carrinho')
    
    return True

def criar_promocoes_categoria(email, categoria_id):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        categoria = categoria.objects.get(id=categoria_id)
    except categoria.DoesNotExist:
        raise ValueError('Categoria não encontrada')
    promocao_categoria = promocao_categoria.objects.create(
        usuario=usuario,
        categoria=categoria,
        data_inicio=timezone.now() 
    )

    return promocao_categoria

def criar_promocoes_condicao(email, condicao_id):
    try:
        usuario = usuario.objects.get(email=email)
    except usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')
    try:
        condicao = condicao.objects.get(id=condicao_id)
    except condicao.DoesNotExist:
        raise ValueError('Categoria não encontrada')
    promocao_condicao = promocao_condicao.objects.create(
        usuario=usuario,
        condicao=condicao,
        data_inicio=timezone.now() 
    )

    return promocao_condicao

def editar_promocoes():
    pass
def remover_promocoes():
    pass
def criar_produto():
    pass
def editar_produto():
    pass
def remover_produto():
    pass
def criar_pedido():
    pass
def editar_pedido():
    pass
def remover_pedido():
    pass
def criar_cupom():
    pass
def editar_cupom():
    pass
def remover_cupom():
    pass