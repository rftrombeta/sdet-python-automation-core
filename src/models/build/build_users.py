from ..dict.dictionary_users import DictionaryUsers
import json


class BuildUsers:

    @staticmethod
    def build_payload():

        return json.loads(json.dumps(DictionaryUsers.dict_users()))
