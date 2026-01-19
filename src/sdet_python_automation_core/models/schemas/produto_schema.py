from typing import Dict, Any
from pydantic import BaseModel, Field
from faker import Faker
from mimesis import Generic
from mimesis.locales import Locale
import random


class ProdutoRequest(BaseModel):
    """
    Model Pydantic para requisição de criação de produto.
    
    Valida nome, preço, descrição e quantidade.
    """
    nome: str = Field(..., min_length=1, description="Nome do produto")
    preco: int = Field(..., gt=0, description="Preço do produto em centavos")
    descricao: str = Field(..., min_length=1, description="Descrição do produto")
    quantidade: int = Field(..., gt=0, description="Quantidade disponível")

    @classmethod
    def generate(
        cls,
        preco_min: int = 1000,
        preco_max: int = 5000,
        quantidade_min: int = 5,
        quantidade_max: int = 10
    ) -> "ProdutoRequest":
        """
        Gera uma instância de ProdutoRequest com dados aleatórios.
        
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
        ProdutoRequest
            Instância com nome, preço, descrição e quantidade gerados automaticamente.
        """
        fake = Faker('pt_BR')
        generic = Generic(Locale.PT_BR)
        
        preco = round(random.uniform(preco_min, preco_max))
        quantidade = round(random.uniform(quantidade_min, quantidade_max))
        
        return cls(
            nome=f"{generic.hardware.cpu()} - R${preco}",
            preco=preco,
            descricao=generic.text.title(),
            quantidade=quantidade
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o model para dicionário.
        
        Returns
        -------
        Dict[str, Any]
            Dicionário com os dados do produto.
        """
        # Compatível com Pydantic v1 e v2
        try:
            return self.model_dump()
        except AttributeError:
            # Fallback para Pydantic v1
            return self.dict()
