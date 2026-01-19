"""
Testes para models e schemas.
"""

from sdet_python_automation_core.models import (
    create_payload_login,
    create_payload_usuario,
    create_payload_produto,
    LoginRequest,
    UsuarioRequest,
    ProdutoRequest,
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
    assert isinstance(payload["administrador"], bool)


def test_create_payload_usuario_administrador():
    """Testa criação de payload de usuário administrador."""
    payload = create_payload_usuario(administrador=True)
    
    assert payload["administrador"] is True


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
    assert isinstance(usuario.administrador, bool)
    
    # Testa conversão para dict
    payload = usuario.to_dict()
    assert isinstance(payload, dict)
    assert isinstance(payload["administrador"], bool)


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
    assert isinstance(payload["preco"], int)
