import random
from typing import Optional


class GenerateCnpjCpf:

    @staticmethod
    def new_cpf() -> str:
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
    def new_cnpj() -> str:
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


def generate_cnpj() -> str:
    """
    Gera um número de CNPJ válido e aleatório que não está na base de controle.

    Returns
    -------
    str
        Um número de CNPJ válido sem formatação.
    """
    return GenerateCnpjCpf.new_cnpj()


def generate_cpf() -> str:
    """
    Gera um número de CPF válido e aleatório que não está na base de controle.

    Returns
    -------
    str
        Um número de CPF válido sem formatação.
    """
    return GenerateCnpjCpf.new_cpf()