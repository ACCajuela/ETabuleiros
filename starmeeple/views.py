from django.shortcuts import render, redirect
from django.http import JsonResponse
from etabuleiros.services import criar_usuario


def home(request):
    return render(request, 'HTML/home.html')

def cadastro(request):
    return render(request, 'HTML/cadastro.html')

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

def painelADM(request):
    return render(request, 'HTML/painelADM.html')

def pedido(request):
    return render(request, 'HTML/pedido.html')

def perfil(request):
    return render(request, 'HTML/perfil.html')

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
        
def desativar_usuario(request):
    if request.method == 'POST':
        user_id = request.user.id 

        try:
            desativar_usuario(user_id)
            return JsonResponse({'status': 'Conta desativada com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)


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

def desativar_usuario(request):
    if request.method == 'POST':
        user_id = request.user.id 

        try:
            desativar_usuario(user_id)
            return JsonResponse({'status': 'Conta desativada com sucesso'})
        except ValueError as e:
            return JsonResponse({'erro': str(e)}, status=400)