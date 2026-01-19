from faker import Faker
import random
from mimesis import Generic
from mimesis.locales import Locale

fake = Faker('pt_BR')
generic = Generic(Locale.PT_BR)

class DictionaryProdutos(dict):

    @staticmethod
    def dict_produtos():
        preco = round(random.uniform(1000, 5000))
        return DictionaryProdutos({
            "nome": f"{generic.hardware.cpu()} - R${preco}",
            "preco": preco,
            "descricao": generic.text.title(),
            "quantidade": round(random.uniform(5, 10))
        })
