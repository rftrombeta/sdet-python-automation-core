from .build.build_login import BuildLogin


def create_payload_login(dict_params):
    """
        Cria o payload padrão para geração de login.
        \n
        Parameters
        ----------
        dict_params: Dicionário com os respectivos parâmetros.\n
            ```
                {
                    "email": "fulano@teste.com.br",
                    "password": "SenhaForte1234"
                }
            ```
        \n
        Returns
        -------
        Payload de login preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildLogin.build_payload(dict_params)
