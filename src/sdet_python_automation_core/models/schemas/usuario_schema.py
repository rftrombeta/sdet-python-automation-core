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
    administrador: str = Field(default="false", description="Indica se o usuário é administrador")

    @field_validator('administrador', mode='before')
    @classmethod
    def validate_administrador(cls, v: Any) -> str:
        """
        Converte valores para as strings "true" ou "false".

        Aceita entradas em string (como "true"/"false", "1"/"0", "yes"/"no"),
        valores booleanos e None. Retorna sempre uma string compatível com a API.
        """
        true_vals = ('true', '1', 'yes')
        false_vals = ('false', '0', 'no')

        if isinstance(v, str):
            s = v.strip().lower()
            if s in true_vals:
                return 'true'
            if s in false_vals:
                return 'false'
            # não reconhecido: mantém a string original (não altera)
            return v
        if v is None:
            return 'false'
        return 'true' if bool(v) else 'false'

    @classmethod
    def generate(cls, administrador: str = "false") -> "UsuarioRequest":
        """
        Gera uma instância de UsuarioRequest com dados aleatórios.
        
        Parameters
        ----------
        administrador : string, optional
            Define se o usuário será administrador. Enviar 'true' ou 'false'. (padrão: false)
            
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
