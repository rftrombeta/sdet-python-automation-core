from typing import Dict, Any
from .schemas.produto_schema import ProdutoRequest


def create_payload_produto(
    preco_min: int = 1000,
    preco_max: int = 5000,
    quantidade_min: int = 5,
    quantidade_max: int = 10
) -> Dict[str, Any]:
    """
    Cria o payload padrão para geração de produto.
    
    Parameters
    ----------
    preco_min : int, optional
        Preço mínimo em centavos (padrão: 1000)
    preco_max : int, optional
        Preço máximo em centavos (padrão: 5000)
    quantidade_min : int, optional
        Quantidade mínima (padrão: 5)
    quantidade_max : int, optional
        Quantidade máxima (padrão: 10)
        
    Returns
    -------
    Dict[str, Any]
        Payload de produto preenchido com informações básicas geradas aleatóriamente.
    """
    produto = ProdutoRequest.generate(
        preco_min=preco_min,
        preco_max=preco_max,
        quantidade_min=quantidade_min,
        quantidade_max=quantidade_max
    )
    return produto.to_dict()
