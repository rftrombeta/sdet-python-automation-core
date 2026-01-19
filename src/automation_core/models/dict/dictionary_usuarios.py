from faker import Faker
fake = Faker('pt_BR')


class DictionaryUsuarios(dict):

    @staticmethod
    def dict_usuarios():
        return DictionaryUsuarios({
            "nome": fake.name(),
            "email": fake.email(),
            "password": fake.password(),
            "administrador": "false"
        })
