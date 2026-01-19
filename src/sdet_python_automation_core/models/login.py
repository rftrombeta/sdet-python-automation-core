from typing import Dict, Any
from .schemas.login_schema import LoginRequest


def create_payload_login() -> Dict[str, Any]:
    """
    Cria o payload padrão para geração de login.
    
    Returns
    -------
    Dict[str, Any]
        Payload de login preenchido com informações básicas geradas aleatóriamente.
    """
    login = LoginRequest.generate()
    return login.to_dict()
