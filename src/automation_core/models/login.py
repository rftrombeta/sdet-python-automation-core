from .build.build_login import BuildLogin


def create_payload_login():
    """
        Cria o payload padrão para geração de login.
        \n
        Returns
        -------
        Payload de login preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildLogin.build_payload()
