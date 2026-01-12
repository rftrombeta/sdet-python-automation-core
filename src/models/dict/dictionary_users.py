from faker import Faker
fake = Faker('pt_BR')


class DictionaryUsers(dict):

    @staticmethod
    def dict_users():
        return DictionaryUsers({
            "nome": fake.name(),
            "email": fake.email(),
            "password": fake.password(),
            "administrador": "false"
        })
