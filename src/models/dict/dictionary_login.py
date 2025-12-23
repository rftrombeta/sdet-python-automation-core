class DictionaryLogin(dict):

    @staticmethod
    def dict_login(email: str, password: str):
        return DictionaryLogin({
            "email": email,
            "password": password
        })
