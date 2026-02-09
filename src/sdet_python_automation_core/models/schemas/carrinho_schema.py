from typing import List, Dict, Any
from pydantic import BaseModel, Field, field_validator


class CarrinhoRequest(BaseModel):
    """
    Model Pydantic para requisição de carrinho de compras.
    
    Valida lista de produtos com ID e quantidade obrigatórios.
    O usuário sempre deve fornecer ambos: idProduto e quantidade.
    """
    produtos: List[Dict[str, Any]] = Field(
        ..., 
        min_length=1, 
        description="Lista de produtos no carrinho com idProduto e quantidade obrigatórios"
    )

    @field_validator('produtos', mode='before')
    @classmethod
    def validate_produtos(cls, v: Any) -> List[Dict[str, Any]]:
        """
        Valida que cada produto tem idProduto E quantidade definidos.
        
        Parameters
        ----------
        v : Any
            Lista de produtos
            
        Returns
        -------
        List[Dict[str, Any]]
            Lista validada de produtos
            
        Raises
        ------
        ValueError
            Se produtos estiver vazio, sem idProduto, sem quantidade ou quantidade <= 0
        """
        if not isinstance(v, list):
            raise ValueError("produtos deve ser uma lista")
        
        for idx, produto in enumerate(v):
            if not isinstance(produto, dict):
                raise ValueError(f"Produto {idx} deve ser um dicionário")
            if 'idProduto' not in produto or not produto['idProduto']:
                raise ValueError(f"Produto {idx} está sem idProduto (obrigatório)")
            if 'quantidade' not in produto:
                raise ValueError(f"Produto {idx} está sem quantidade (obrigatório)")
            if produto['quantidade'] <= 0:
                raise ValueError(f"Produto {idx} deve ter quantidade > 0")
        
        return v

    @classmethod
    def generate(cls, produtos: List[Dict[str, Any]]) -> "CarrinhoRequest":
        """
        Gera uma instância de CarrinhoRequest com produtos obrigatórios.
        
        O usuário DEVE fornecer a lista de produtos com idProduto e quantidade.
        
        Parameters
        ----------
        produtos : List[Dict[str, Any]]
            Lista obrigatória com TODOS os produtos contendo idProduto e quantidade.
            Exemplo: [
                {"idProduto": "ABC123", "quantidade": 2},
                {"idProduto": "DEF456", "quantidade": 1}
            ]
            
        Returns
        -------
        CarrinhoRequest
            Instância com lista de produtos fornecidos.
            
        Raises
        ------
        ValueError
            Se produtos estiver vazio ou inválido
            
        Example
        -------
        >>> produtos = [
        ...     {"idProduto": "BeeJh5lz3k6kSIzA", "quantidade": 1},
        ...     {"idProduto": "YaeJ455lz3k6kSIzA", "quantidade": 3}
        ... ]
        >>> carrinho = CarrinhoRequest.generate(produtos=produtos)
        >>> payload = carrinho.to_dict()
        """
        if not produtos:
            raise ValueError("produtos é obrigatório e não pode estar vazio")
        
        return cls(produtos=produtos)

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o model para dicionário.
        
        Returns
        -------
        Dict[str, Any]
            Dicionário com os dados do carrinho.
        """
        try:
            return self.model_dump()
        except AttributeError:
            return self.dict()
        except AttributeError:
            return self.dict()
