from ..dict.dictionary_login import DictionaryLogin
import json


class BuildLogin:

    @staticmethod
    def build_payload():

        return json.loads(json.dumps(DictionaryLogin.dict_login()))
