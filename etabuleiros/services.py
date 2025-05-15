from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
from django.core.exceptions import ValidationError
from django.utils import timezone
from etabuleiros.models import Usuario, Produto, Categoria, CupomDesconto, Promocao, ListaDesejos, Pedido, CarrinhoCompras, Devolucao, Duvida, Fornecedor, Frete, Editora, Notificacao

def get_usuario_por_id(usuario_id):
    try:
        return Usuario.objects.get(id = usuario_id)
    except Usuario.DoesNotExist:
        raise ValueError('Usuário não encontrado')

def get_produto_por_id(produto_id):
    try:
        return Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        raise ValueError('Produto não encontrado')
    
def get_categoria_por_id(categoria_id):
    try:
        return Categoria.objects.get(id=categoria_id)
    except Categoria.DoesNotExist:
        raise ValueError('Categoria não encontrada')
    
def get_cupom_por_id(cupom_id):
    try:
        return CupomDesconto.objects.get(id=cupom_id)
    except CupomDesconto.DoesNotExist:
        raise ValueError('Cupom não encontrado')
    
def get_promocao_por_id(promocao_id):
    try:
        return Promocao.objects.get(id=promocao_id)
    except Promocao.DoesNotExist:
        raise ValueError('Promoção não encontrada')
    
def get_lista_por_id(lista_id):
    try:
        return ListaDesejos.objects.get(id=lista_id)
    except ListaDesejos.DoesNotExist:
        raise ValueError('Lista não encontrada')
    
def get_pedido_por_id(pedido_id):
    try:
        return Pedido.objects.get(id=pedido_id)
    except Pedido.DoesNotExist:
        raise ValueError('Pedido não encontrado')

def get_carrinho_por_id(carrinho_id):
    try:
        return CarrinhoCompras.objects.get(id=carrinho_id)
    except CarrinhoCompras.DoesNotExist:
        raise ValueError('Carrinho não encontrado')


def get_devolucao_por_id(devolucao_id):
    try:
        return Devolucao.objects.get(id=devolucao_id)
    except Devolucao.DoesNotExist:
        raise ValueError('Devolucao não encontrada')
    
def get_duvida_por_id(duvida_id):
    try:
        return Duvida.objects.get(id=duvida_id)
    except Duvida.DoesNotExist:
        raise ValueError('Duvida não encontrada')
    
def get_fornecedor_por_id(fornecedor_id):
    try:
        return Fornecedor.objects.get(id=fornecedor_id)
    except Fornecedor.DoesNotExist:
        raise ValueError('Fornecedor não encontrado')
    
def get_frete_por_id(frete_id):
    try:
        return Frete.objects.get(id=frete_id)
    except Frete.DoesNotExist:
        raise ValueError('Frete não encontrada')
    
def get_editora_por_id(editora_id):
    try:
        return Editora.objects.get(id=editora_id)
    except Editora.DoesNotExist:
        raise ValueError('Editora não encontrada')
    
def get_notificacao_por_id(notificacao_id):
    try:
        return Notificacao.objects.get(id=notificacao_id)
    except Notificacao.DoesNotExist:
        raise ValueError('Notificacao não encontrada')
    
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

#Parte Carrinho   
def incluir_item_no_carrinho(usuario_id, produto_id, quantidade):
    usuario = get_usuario_por_id(usuario_id)
    produto = get_produto_por_id(produto_id)
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError('A quantidade deve ser maior que zero')
    except ValueError:
        raise ValueError('Quantidade inválida')
    carrinho = carrinho.objects.create(
        usuario=usuario,
        produto=produto,
        quantidade=quantidade,
        data=timezone.now()  
    )
    return carrinho

def atualizar_item_carrinho(usuario_id, produto_id, quantidade, nova_quantidade):
    usuario = get_usuario_por_id(usuario_id)
    produto = get_produto_por_id(produto_id)
    try:
        quantidade += int(nova_quantidade)
        if nova_quantidade <= 0:
            raise ValueError('A quantidade deve ser maior que zero')
    except ValueError:
        raise ValueError('Quantidade inválida')
    try:
        carrinho = carrinho.objects.get(usuario=usuario, produto=produto)
        carrinho.quantidade = nova_quantidade
        carrinho.save()
    except carrinho.DoesNotExist:
        raise ValueError('Carrinho não encontrado')
    return carrinho

def remover_item_carrinho(usuario_id, produto_id, quantidade):
    usuario = get_usuario_por_id(usuario_id)
    produto = get_produto_por_id(produto_id)
    try:
        quantidade = 0
    except ValueError:
        raise ValueError('Quantidade inválida')
    try:
        carrinho = carrinho.objects.get(usuario=usuario, produto=produto)
        carrinho.save()
    except carrinho.DoesNotExist:
        raise ValueError('Carrinho não encontrado')
    
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
