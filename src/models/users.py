from .build.build_users import BuildUsers


def create_payload_users(dict_params):
    """
        Cria o payload padrão para geração de login.
        \n
        Parameters
        ----------
        dict_params: Dicionário com os respectivos parâmetros.\n
            ```
                {
                    "nome": "Fulano da Silva",
                    "email": "beltrano@qa.com.br",
                    "password": "SenhaForte1234",
                    "administrador": "true"
                }
            ```
        \n
        Returns
        -------
        Payload de login preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildUsers.build_payload(dict_params)
