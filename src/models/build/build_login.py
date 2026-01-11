from ..dict.dictionary_login import DictionaryLogin
import json


class BuildLogin:

    @staticmethod
    def build_payload(dict_params):

        payload = DictionaryLogin.dict_login(dict_params["email"], dict_params["password"])

        return json.loads(json.dumps(payload))
