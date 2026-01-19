from .build.build_usuarios import BuildUsuarios


def create_payload_usuario():
    """
        Cria o payload padrão para geração de usuário.
        \n
        Returns
        -------
        Payload de usuário preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildUsuarios.build_payload()
