from faker import Faker
fake = Faker('pt_BR')


class DictionaryUsers(dict):

    @staticmethod
    def dict_users():
        return DictionaryUsers({
            "nome": fake.full_name(),
            "email": fake.email(),
            "password": fake.password(),
            "administrador": fake.boolean()
        })
