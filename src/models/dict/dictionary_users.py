class DictionaryUsers(dict):

    @staticmethod
    def dict_users(nome: str, email: str, password: str, administrador: str):
        return DictionaryUsers({
            "nome": nome,
            "email": email,
            "password": password,
            "administrador": administrador
        })
