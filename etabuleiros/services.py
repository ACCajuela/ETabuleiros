from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.utils import timezone

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

def login (request,email,senha):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("Email não cadastrado")
    
    user = authenticate(request, username=user.email, password=senha)
    
    if user is not None:
        login(request, user)
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

