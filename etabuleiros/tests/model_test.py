
import pytest
from unittest.mock import patch, MagicMock
from datetime import date
from etabuleiros.models import Usuario, Produto, Categoria, Editora, Promocao, CarrinhoCompras, AvalicaoProduto


#Teste de Integração
@pytest.mark.labbd2
def test_criar_produto_integracao():
    data_criacao = date(2012, 3, 23)

    categoria = Categoria.objects.create(
        nome="Mais 18"
    )
    
    editora = Editora.objects.create(
        nome="Tristeza"
    )

    produto = Produto.objects.create(
        nome="Nome de Jogo",
        qtd=30,
        preco=5.90,
        cat=categoria,
        editora=editora,
        tempo_de_jogo=4,
        numero_jogadores="8",
        itens_inclusos="A, B, C, D, E",
        descri="É um jogo",
        recomendado=False,
        clas_ind='18',
        autor="Fulano",
        data_criacao=data_criacao
    )

    assert produto.nome == "Nome de Jogo"
    assert produto.qtd == 30
    assert produto.preco == 5.90
    assert produto.cat.nome == "Mais 18"
    assert produto.editora.nome == "Tristeza"
    assert produto.tempo_de_jogo == 4
    assert produto.numero_jogadores == "8"
    assert produto.itens_inclusos == "A, B, C, D, E"
    assert produto.descri == "É um jogo"
    assert produto.recomendado is False
    assert produto.clas_ind == '18'
    assert produto.autor == "Fulano"
    assert produto.data_criacao == data_criacao

@pytest.mark.labbd2
def test_carrinho_integracao():
    data_adicao = (1999, 7, 13)

    produto = Produto.objects.create(
        nome="Nome de Jogo",
        qtd=30,
        preco=5.90,
        cat=categoria,
        editora=editora,
        tempo_de_jogo=4,
        numero_jogadores="8",
        itens_inclusos="A, B, C, D, E",
        descri="É um jogo",
        recomendado=False,
        clas_ind='18',
        autor="Fulano",
        data_criacao=data_criacao
    )

    usuario = Usuario.objects.create(
        nome="Pantaleão",
        email="pantaleao@gmail.com",
        cpf="333.333.333-3",
        dataNasc=180219999,
        telefone="(19) 99871-4356",
        endereco="rua galvao"
    )    

    carrinho = CarrinhoCompras.objects.create(
        user=usuario,
        produto=produto,
        quantidade=10,
        data_adicao=data_adicao
    )

    assert user=usuario
    assert produto=produto
    assert quantidade=quantidade
    assert data_adicao=data_adicao

@pytest.mark.labbd2
def test_avaliar_produto_integracao():
    data_avaliacao=(2003, 8, 17)
    produto = Produto.objects.create(
        nome="Nome de Jogo",
        qtd=30,
        preco=5.90,
        cat=categoria,
        editora=editora,
        tempo_de_jogo=4,
        numero_jogadores="8",
        itens_inclusos="A, B, C, D, E",
        descri="É um jogo",
        recomendado=False,
        clas_ind='18',
        autor="Fulano",
        data_criacao=data_criacao
    )

    usuario = Usuario.objects.create(
        nome="Pantaleão",
        email="pantaleao@gmail.com",
        cpf="333.333.333-3",
        dataNasc=180219999,
        telefone="(19) 99871-4356",
        endereco="rua galvao"
    )   

    avaliacao = AvaliacaoProduto.objects.crate(
        ava_prod = produto
        ava_user = usuario
        nota = 4.2
        comentario = "Uau! Muito giro!"
        data_avalicao=data_avalicao
    )

    assert ava_prod = produto
    assert ava_user = usuario
    assert nota = 4.2
    assert comentario = "Uau! Muito giro!"
    assert data_avaliacao = data_avaliacao

#Testes unitarios
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
    data_criacao = date(2012, 3, 23)

    mock_categoria = MagicMock(spec=Categoria)
    mock_categoria.id = 1
    mock_categoria.nome = "Mais 18"

    mock_editora = MagicMock(spec=Editora)
    mock_editora.id = 1
    mock_editora.nome = "Tristeza"

    mock_produto = MagicMock(spec=Produto)
    mock_produto.nome = "Nome de Jogo"
    mock_produto.qtd = 30
    mock_produto.preco = 5.90
    mock_produto.cat = mock_categoria
    mock_produto.editora = mock_editora
    mock_produto.tempo_de_jogo = 4
    mock_produto.numero_jogadores = "8"
    mock_produto.itens_inclusos = "A, B, C, D, E"
    mock_produto.descri = "É um jogo"
    mock_produto.recomendado = False
    mock_produto.clas_ind = '18'
    mock_produto.autor = "Fulano"
    mock_produto.data_criacao = data_criacao

    with patch('etabuleiros.models.Produto.objects.create', return_value=mock_produto) as mock_create:
        produto = Produto.objects.create(
            nome="Nome de Jogo",
            qtd=30,
            preco=5.90,
            cat=mock_categoria,
            editora=mock_editora,
            tempo_de_jogo=4,
            numero_jogadores="8",
            itens_inclusos="A, B, C, D, E",
            descri="É um jogo",
            recomendado=False,
            clas_ind='18',
            autor="Fulano",
            data_criacao=data_criacao
        )

        mock_create.assert_called_once_with(
            nome="Nome de Jogo",
            qtd=30,
            preco=5.90,
            cat=mock_categoria,
            editora=mock_editora,
            tempo_de_jogo=4,
            numero_jogadores="8",
            itens_inclusos="A, B, C, D, E",
            descri="É um jogo",
            recomendado=False,
            clas_ind='18',
            autor="Fulano",
            data_criacao=data_criacao
        )

        assert produto.nome == "Nome de Jogo"
        assert produto.cat.nome == "Mais 18"
        assert produto.editora.nome == "Tristeza"
        assert produto.data_criacao == data_criacao
        assert produto.recomendado is False

def criar_promocao_unitario():
    data_criacao = date(2025, 2, 15)
    data_fim = date(2025, 8, 3)
    
    mock_promocao = MagicMock(speck=Promocao)
    mock_promocao.nome = "Promocao Primavera"
    mock_promocao.decimal = 4.5
    mock_promocao.data_inicio = data_criacao
    mock_promocao.data_fim = data_fim

        with patch('etabuleiros.models.Promocao.objects.create', return_value=mock_promocao) as mock_create:
        promocao = Promocao.objects.create(
            nome="Promocao Primavera",
            decimal=4.5,
            data_inicio=data_criacao,
            data_fim=data_fim
        )

        mock_create.assert_called_once_with(
            nome="Promocao Primavera",
            decimal=4.5,
            data_inicio=data_criacao,
            data_fim=data_fim
        )

        assert promocao.nome == "Promocao Primavera"
        assert promocao.decimal == 4.5
        assert promocao.data_inicio == data_criacao
        assert promocao.data_fim == data_fimS
    