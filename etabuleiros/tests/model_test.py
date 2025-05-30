
import pytest
from unittest.mock import patch, MagicMock
from etabuleiros.models import Usuario, Produto

@pytest.mark.django_db
def test_criar_usuario_integração():
    usuario = Usuario.objects.create(nome="Pantaleão", email="pantaleao@gmail.com", cpf="333.333.333-3", dataNasc=180219999, telefone = "(19) 99871-4356", endereco="rua galvao")
    assert usuario.nome == "Pantaleão"
    assert usuario.email == "pantaleao@gmail.com"
    assert usuario.cpf == "333.333.333-3"
    assert usuario.dataNasc == 180219999
    assert usuario.telefone == "(19) 99871-4356"
    assert usuario.endereco == "rua galvao"

def test_criar_produto_integração():
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


def test_criar_promocao_integração(nome_promocao=" ", desconto= , data_inicio= , data_fim= ):
    promocao = Promocao.objects.create()
    assert promocao.nome_promocao == 
    assert promocao.desconto == 
    assert promocao.data_inicio ==
    assert promocao.data_fim ==

def test_criar_usuario_unitario():
    mock_usuario = MagicMock(spec=Usuario)
    mock_usuario.nome = "Pantaleão"
    mock_usuario.email = "pantaleao@gmail.com"
    mock_usuario.cpf = "333.333.333-3"
    mock_usuario.dataNasc = 180219999
    mock_usuario.telefone = "(19) 99871-4356"
    mock_usuario.endereco = "rua galvao"

    with patch('etabuleiros.models.Usuario.objects.create', return_value=mock_usuario) as mock_create:
        usuario = Usuario.objects.create(
            nome="Pantaleão",
            email="pantaleao@gmail.com",
            cpf="333.333.333-3",
            dataNasc=180219999,
            telefone="(19) 99871-4356",
            endereco="rua galvao"
        )

        mock_create.assert_called_once_with(
            nome="Pantaleão",
            email="pantaleao@gmail.com",
            cpf="333.333.333-3",
            dataNasc=180219999,
            telefone="(19) 99871-4356",
            endereco="rua galvao"
        )

        assert usuario.nome == "Pantaleão"
        assert usuario.email == "pantaleao@gmail.com"
        assert usuario.cpf == "333.333.333-3"
        assert usuario.dataNasc == 180219999
        assert usuario.telefone == "(19) 99871-4356"
        assert usuario.endereco == "rua galvao"

def criar_produto_unitario():
    mock_produto = MagicMock(spec=Produto)
    mock_produto.nome = "Nome de Jogo"
    mock_produto.qtd = 30
    mock_produto.preco = 5.90
    mock_produto.cat