from django.shortcuts import render

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


