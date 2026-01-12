from faker import Faker
import random
from mimesis import Generic
from mimesis.locales import Locale

fake = Faker('pt_BR')
generic = Generic(Locale.PT_BR)

class DictionaryProdutos(dict):

    @staticmethod
    def dict_produtos():
        return DictionaryProdutos({
            "nome": generic.hardware.cpu(),
            "preco": round(random.uniform(1000, 5000)),
            "descricao": generic.text.title(),
            "quantidade": round(random.uniform(5, 10))
        })
