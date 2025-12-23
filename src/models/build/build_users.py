from ..dict.dictionary_users import DictionaryUsers
import json


class BuildUsers:

    @staticmethod
    def build_payload(dict_params):

        payload = {DictionaryUsers.dict_users(
            dict_params["nome"],
            dict_params["email"],
            dict_params["password"],
            dict_params["administrador"]
        )}

        return json.loads(json.dumps(payload))
