from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import logout

def criar_usuario(nome, email, senha):
    if User.objects.filter(email=email).exists():
        raise ValueError("Email já cadastrado")

    usuario = [
        username = email,
        email = email,
        password = senha,
        first_name = nome
    ]

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
    # Verifica se o usuário existe
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("Email não cadastrado")
    
    # Autentica o usuário
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
    
