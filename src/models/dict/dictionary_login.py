from fakers import generate_email


class DictionaryLogin(dict):

    @staticmethod
    def dict_login():
        """
        Retorna um dicionário de login. Se `email` for None ou vazio,
        gera um e-mail aleatório usando `generate_email`.
        """
        if not email:
            email = generate_email()
        return DictionaryLogin({
            "email": generate_email(),
            "password": password
        })
