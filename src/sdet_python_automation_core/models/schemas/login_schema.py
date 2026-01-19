from typing import Dict, Any
from pydantic import BaseModel, EmailStr, Field
from faker import Faker


class LoginRequest(BaseModel):
    """
    Model Pydantic para requisição de login.
    
    Valida email e senha conforme os contratos da API.
    """
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=1, description="Senha do usuário")

    @classmethod
    def generate(cls) -> "LoginRequest":
        """
        Gera uma instância de LoginRequest com dados aleatórios.
        
        Returns
        -------
        LoginRequest
            Instância com email e senha gerados automaticamente.
        """
        fake = Faker('pt_BR')
        return cls(
            email=fake.email(),
            password=fake.password()
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o model para dicionário.
        
        Returns
        -------
        Dict[str, Any]
            Dicionário com os dados do login.
        """
        # Compatível com Pydantic v1 e v2
        try:
            return self.model_dump()
        except AttributeError:
            # Fallback para Pydantic v1
            return self.dict()
