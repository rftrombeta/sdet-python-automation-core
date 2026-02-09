from typing import Dict, Any
from .schemas.usuario_schema import UsuarioRequest


def create_payload_usuario(administrador: str = "false") -> Dict[str, Any]:
    """
    Cria o payload padrão para geração de usuário.
    
    Parameters
    ----------
    administrador : string, optional
        Define se o usuário será administrador. Enviar 'true' ou 'false'. (padrão: false)
        
    Returns
    -------
    Dict[str, Any]
        Payload de usuário preenchido com informações básicas geradas aleatóriamente.
    """
    usuario = UsuarioRequest.generate(administrador=administrador)
    return usuario.to_dict()
