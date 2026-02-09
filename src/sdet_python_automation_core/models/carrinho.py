from typing import Dict, Any, List
from .schemas.carrinho_schema import CarrinhoRequest


def create_payload_carrinho(produtos: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Cria o payload de carrinho de compras com produtos obrigatórios.
    
    O usuário DEVE fornecer a lista completa de produtos com idProduto e quantidade.
    
    Parameters
    ----------
    produtos : List[Dict[str, Any]]
        Lista obrigatória com todos os produtos contendo idProduto e quantidade.
        O usuário deve definir ambos os parâmetros para cada produto.
        
    Returns
    -------
    Dict[str, Any]
        Payload de carrinho preenchido com produtos fornecidos.
        
    Example
    -------
    >>> produtos = [
    ...     {"idProduto": "BeeJh5lz3k6kSIzA", "quantidade": 1},
    ...     {"idProduto": "YaeJ455lz3k6kSIzA", "quantidade": 3}
    ... ]
    >>> payload = create_payload_carrinho(produtos=produtos)
    
    Raises
    ------
    ValueError
        Se produtos estiver vazio ou sem os campos obrigatórios
    """
    carrinho = CarrinhoRequest.generate(produtos=produtos)
    return carrinho.to_dict()
