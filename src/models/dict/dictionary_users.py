class DictionaryUsers(dict):

    @staticmethod
    def dict_users(name: str, email: str, password: str, administrator: str):
        return DictionaryUsers({
            "nome": name,
            "email": email,
            "password": password,
            "administrador": administrator
        })
