from ..dict.dictionary_produtos import DictionaryProdutos
import json


class BuildProdutos:

    @staticmethod
    def build_payload():

        return json.loads(json.dumps(DictionaryProdutos.dict_produtos()))
