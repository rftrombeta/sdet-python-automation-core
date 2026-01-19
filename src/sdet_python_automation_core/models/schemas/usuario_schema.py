from typing import Dict, Any
from pydantic import BaseModel, EmailStr, Field, field_validator
from faker import Faker


class UsuarioRequest(BaseModel):
    """
    Model Pydantic para requisição de criação de usuário.
    
    Valida nome, email, senha e status de administrador.
    """
    nome: str = Field(..., min_length=1, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=1, description="Senha do usuário")
    administrador: bool = Field(default=False, description="Indica se o usuário é administrador")

    @field_validator('administrador', mode='before')
    @classmethod
    def validate_administrador(cls, v: Any) -> bool:
        """
        Converte string "true"/"false" para boolean se necessário.
        
        Parameters
        ----------
        v : Any
            Valor a ser validado
            
        Returns
        -------
        bool
            Valor boolean
        """
        if isinstance(v, str):
            return v.lower() in ('true', '1', 'yes')
        return bool(v)

    @classmethod
    def generate(cls, administrador: bool = False) -> "UsuarioRequest":
        """
        Gera uma instância de UsuarioRequest com dados aleatórios.
        
        Parameters
        ----------
        administrador : bool, optional
            Define se o usuário será administrador (padrão: False)
            
        Returns
        -------
        UsuarioRequest
            Instância com nome, email, senha e status gerados automaticamente.
        """
        fake = Faker('pt_BR')
        return cls(
            nome=fake.name(),
            email=fake.email(),
            password=fake.password(),
            administrador=administrador
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o model para dicionário.
        
        Returns
        -------
        Dict[str, Any]
            Dicionário com os dados do usuário.
        """
        # Compatível com Pydantic v1 e v2
        try:
            return self.model_dump()
        except AttributeError:
            # Fallback para Pydantic v1
            return self.dict()
