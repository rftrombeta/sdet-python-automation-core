from ..dict.dictionary_usuarios import DictionaryUsuarios
import json


class BuildUsuarios:

    @staticmethod
    def build_payload():

        return json.loads(json.dumps(DictionaryUsuarios.dict_users()))
