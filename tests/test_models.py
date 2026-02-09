"""
Testes para models e schemas.
"""

from sdet_python_automation_core.models import (
    create_payload_login,
    create_payload_usuario,
    create_payload_produto,
    create_payload_carrinho,
    LoginRequest,
    UsuarioRequest,
    ProdutoRequest,
    CarrinhoRequest,
)


def test_create_payload_login():
    """Testa criação de payload de login."""
    payload = create_payload_login()
    
    assert isinstance(payload, dict)
    assert "email" in payload
    assert "password" in payload
    assert "@" in payload["email"]


def test_create_payload_usuario():
    """Testa criação de payload de usuário."""
    payload = create_payload_usuario()
    
    assert isinstance(payload, dict)
    assert "nome" in payload
    assert "email" in payload
    assert "password" in payload
    assert "administrador" in payload
    assert isinstance(payload["administrador"], str)
    assert payload["administrador"] in ("true", "false")


def test_create_payload_usuario_administrador():
    """Testa criação de payload de usuário administrador."""
    payload = create_payload_usuario(administrador=True)
    
    assert payload["administrador"] == "true"


def test_create_payload_produto():
    """Testa criação de payload de produto."""
    payload = create_payload_produto()
    
    assert isinstance(payload, dict)
    assert "nome" in payload
    assert "preco" in payload
    assert "descricao" in payload
    assert "quantidade" in payload
    assert isinstance(payload["preco"], int)
    assert isinstance(payload["quantidade"], int)
    assert payload["preco"] > 0
    assert payload["quantidade"] > 0


def test_login_request_model():
    """Testa model Pydantic LoginRequest."""
    login = LoginRequest.generate()
    
    assert isinstance(login, LoginRequest)
    assert "@" in login.email
    assert len(login.password) > 0
    
    # Testa conversão para dict
    payload = login.to_dict()
    assert isinstance(payload, dict)
    assert "email" in payload
    assert "password" in payload


def test_usuario_request_model():
    """Testa model Pydantic UsuarioRequest."""
    usuario = UsuarioRequest.generate()
    
    assert isinstance(usuario, UsuarioRequest)
    assert len(usuario.nome) > 0
    assert "@" in usuario.email
    assert isinstance(usuario.administrador, str)
    assert usuario.administrador in ("true", "false")
    
    # Testa conversão para dict
    payload = usuario.to_dict()
    assert isinstance(payload, dict)
    assert isinstance(payload["administrador"], str)


def test_produto_request_model():
    """Testa model Pydantic ProdutoRequest."""
    produto = ProdutoRequest.generate()
    
    assert isinstance(produto, ProdutoRequest)
    assert len(produto.nome) > 0
    assert produto.preco > 0
    assert produto.quantidade > 0
    
    # Testa conversão para dict
    payload = produto.to_dict()
    assert isinstance(payload, dict)


def test_create_payload_carrinho():
    """Testa criação de payload de carrinho com produtos obrigatórios."""
    produtos = [
        {"idProduto": "BeeJh5lz3k6kSIzA", "quantidade": 1},
        {"idProduto": "YaeJ455lz3k6kSIzA", "quantidade": 3}
    ]
    payload = create_payload_carrinho(produtos=produtos)
    
    assert isinstance(payload, dict)
    assert "produtos" in payload
    assert isinstance(payload["produtos"], list)
    assert len(payload["produtos"]) == 2
    
    # Testa estrutura e valores
    for idx, produto in enumerate(payload["produtos"]):
        assert "idProduto" in produto
        assert "quantidade" in produto
        assert produto["idProduto"] == produtos[idx]["idProduto"]
        assert produto["quantidade"] == produtos[idx]["quantidade"]


def test_create_payload_carrinho_multiplos():
    """Testa criação de payload de carrinho com múltiplos produtos."""
    produtos = [
        {"idProduto": "ABC123", "quantidade": 2},
        {"idProduto": "DEF456", "quantidade": 1},
        {"idProduto": "GHI789", "quantidade": 5},
        {"idProduto": "JKL012", "quantidade": 3},
        {"idProduto": "MNO345", "quantidade": 4}
    ]
    payload = create_payload_carrinho(produtos=produtos)
    
    assert len(payload["produtos"]) == 5
    
    # Testa que cada produto está com os valores corretos
    for idx, produto in enumerate(payload["produtos"]):
        assert produto["idProduto"] == produtos[idx]["idProduto"]
        assert produto["quantidade"] == produtos[idx]["quantidade"]


def test_carrinho_request_model():
    """Testa model Pydantic CarrinhoRequest."""
    produtos = [
        {"idProduto": "ABC123", "quantidade": 2},
        {"idProduto": "DEF456", "quantidade": 1}
    ]
    carrinho = CarrinhoRequest.generate(produtos=produtos)
    
    assert isinstance(carrinho, CarrinhoRequest)
    assert len(carrinho.produtos) == 2
    
    for idx, produto in enumerate(carrinho.produtos):
        assert isinstance(produto, dict)
        assert "idProduto" in produto
        assert "quantidade" in produto
        assert produto["idProduto"] == produtos[idx]["idProduto"]
        assert produto["quantidade"] == produtos[idx]["quantidade"]
    
    # Testa conversão para dict
    payload = carrinho.to_dict()
    assert isinstance(payload, dict)
    assert "produtos" in payload
    assert isinstance(payload["produtos"], list)


def test_carrinho_request_validacao():
    """Testa validação do modelo CarrinhoRequest."""
    import pytest
    from pydantic import ValidationError
    
    # Testa erro quando produtos está vazio
    with pytest.raises(ValidationError):
        CarrinhoRequest(produtos=[])
    
    # Testa erro quando produto sem idProduto
    with pytest.raises(ValidationError):
        CarrinhoRequest(produtos=[{"quantidade": 1}])
    
    # Testa erro quando produto sem quantidade
    with pytest.raises(ValidationError):
        CarrinhoRequest(produtos=[{"idProduto": "ABC123"}])
    
    # Testa erro quando quantidade é 0
    with pytest.raises(ValidationError):
        CarrinhoRequest(produtos=[{"idProduto": "ABC123", "quantidade": 0}])
    
    # Testa sucesso com dados válidos
    carrinho = CarrinhoRequest(
        produtos=[{"idProduto": "ABC123", "quantidade": 1}]
    )
    assert isinstance(carrinho, CarrinhoRequest)


def test_carrinho_request_generate_obrigatorio():
    """Testa que generate() exige produtos com ambos os parâmetros."""
    import pytest
    
    # Testa erro quando produtos vazio
    with pytest.raises(ValueError):
        CarrinhoRequest.generate(produtos=[])
    
    # Testa sucesso com lista de produtos completa
    produtos = [
        {"idProduto": "ID001", "quantidade": 5},
        {"idProduto": "ID002", "quantidade": 10}
    ]
    carrinho = CarrinhoRequest.generate(produtos=produtos)
    
    assert len(carrinho.produtos) == 2
    assert carrinho.produtos[0]["idProduto"] == "ID001"
    assert carrinho.produtos[0]["quantidade"] == 5
