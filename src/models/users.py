from .build.build_users import BuildUsers


def create_payload_users():
    """
        Cria o payload padrão para geração de login.
        \n
        Returns
        -------
        Payload de login preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildUsers.build_payload()
