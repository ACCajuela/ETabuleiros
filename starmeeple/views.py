from django.shortcuts import render

def home(request):
    return render(request, 'HTML/home.html')

def editCliente(request):
    return render(request, 'HTML/editCliente.html')

def editFuncionarioAdm(request):
    return render(request, 'HTML/editFuncionarioAdm.html')

def login(request):
    return render(request, 'HTML/login.html')

def pedido(request):
    return render(request, 'HTML/pedido.html')


