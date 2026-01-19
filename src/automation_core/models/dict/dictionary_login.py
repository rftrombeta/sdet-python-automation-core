from faker import Faker
fake = Faker('pt_BR')


class DictionaryLogin(dict):

    @staticmethod
    def dict_login():
        """
        Retorna um dicionário de login. Se `email` for None ou vazio,
        gera um e-mail aleatório usando `generate_email`.
        """
        return DictionaryLogin({
            "email": fake.email(),
            "password": fake.password()
        })
