
import pytest
from etabuleiros.models import Usuario, Produto

@pytest.mark.django_db
def test_criar_usuario():
    usuario = Usuario.objects.create(nome="Pantaleão", email="pantaleao@gmail.com", cpf="333.333.333-3", dataNasc=180219999, telefone = "(19) 99871-4356", endereco="rua galvao")
    assert usuario.nome == "Pantaleão"
    assert usuario.email == "pantaleao@gmail.com"
    assert usuario.cpf == "333.333.333-3"
    assert usuario.dataNasc == 180219999
    assert usuario.telefone == "(19) 99871-4356"
    assert usuario.endereco == "rua galvao"

def test_criar_produto():
    produto = Produto.objetcts.crete(nome="", qtd = , preco = , cat = , editora = , tempo_de_jogo = , numero_jogadores = , itens_inclusos = " ", descri = " ", recomendado = , clas_ind = , autor = " ", data_criacao = )
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 
    assert produto.nome == 


def test_criar_promocao(nome_promocao=" ", desconto= , data_inicio= , data_fim= ):
    promocao = Promocao.objects.create()
    assert promocao.nome_promocao == 
    assert promocao.desconto == 
    assert promocao.data_inicio ==
    assert promocao.data_fim ==

