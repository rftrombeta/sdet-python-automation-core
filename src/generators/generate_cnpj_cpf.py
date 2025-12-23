import random
from ..requests import get_help


class GenerateCnpjCpf:

    @staticmethod
    def new_cpf():
        """
        Gera um novo CPF (Cadastro de Pessoas Físicas) aleatório.

        :return: Um número de CPF válido sem formatação.
        :rtype: str
        """
        cpf = [random.randrange(10) for _ in range(9)]
        for _ in range(2):
            value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
            cpf.append(11 - value if value > 1 else 0)
        return "".join(str(x) for x in cpf)

    @staticmethod
    def new_cnpj():
        """
        Gera um novo CNPJ (Cadastro Nacional da Pessoa Jurídica) aleatório.

        :return: Um número de CNPJ válido sem formatação.
        :rtype: str
        """
        cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]
        for _ in range(2):
            value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
            digit = 11 - value % 11
            cnpj.append(digit if digit < 10 else 0)
        return "".join(str(x) for x in cnpj)


def generate_cnpj():
    """
    Gera um número de CNPJ válido e aleatório que não está na base de controle.

    :return: Um número de CNPJ válido sem formatação.
    :rtype: str
    :raises Exception: Se não for possível encontrar um CNPJ que não esteja na base de controle.
    """
    for _ in range(10):
        cnpj = GenerateCnpjCpf.new_cnpj()
        if get_help.get_document_number_cache_base_control(cnpj) == 204:
            return cnpj
    raise Exception('Failed to find a CNPJ not in the control base. Please try again!')


def generate_cpf():
    """
    Gera um número de CPF válido e aleatório que não está na base de controle.

    :return: Um número de CPF válido sem formatação.
    :rtype: str
    :raises Exception: Se não for possível encontrar um CPF que não esteja na base de controle.
    """
    for _ in range(10):
        cpf = GenerateCnpjCpf.new_cpf()
        if get_help.get_document_number_cache_base_control(cpf) == 204:
            return cpf
    raise Exception('Failed to find a CPF not in the control base. Please try again!')
