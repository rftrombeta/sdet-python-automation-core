from datetime import datetime, timedelta
from random import choice
from typing import Literal


def generate_current_date() -> str:
    """
    Retorna a data atual no formato yyyy-mm-dd.

    :return: Data atual no formato yyyy-mm-dd.
    :rtype: str
    """
    return datetime.now().astimezone().strftime('%Y-%m-%d')


def generate_current_date_hour() -> str:
    """
    Retorna a data e hora atual no formato yyyy-mm-dd hh:mm:ss.f.

    :return: Data e hora atual no formato yyyy-mm-dd hh:mm:ss.f.
    :rtype: str
    """
    return datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f')


def generate_date_plus_n_days(days: int) -> str:
    """
    Gera uma data adicionando uma quantidade especificada de dias à data atual.

    :param days: Quantidade de dias para adicionar.
    :type days: int
    :return: A data atual mais a quantidade especificada de dias no formato yyyy-mm-dd.
    :rtype: str
    """
    return (datetime.now() + timedelta(int(days))).astimezone().strftime('%Y-%m-%d')


def generate_date_minus_n_days(days: int) -> str:
    """
    Gera uma data subtraindo uma quantidade especificada de dias da data atual.

    :param days: Quantidade de dias para subtrair.
    :type days: int
    :return: A data atual menos a quantidade especificada de dias no formato yyyy-mm-dd.
    :rtype: str
    """
    return (datetime.now() - timedelta(int(days))).astimezone().strftime('%Y-%m-%d')


def increment_date_n_days(date: str, days: int) -> str:
    """
    Incrementa uma data fornecida por uma quantidade especificada de dias.

    :param date: A data inicial no formato yyyy-mm-dd.
    :type date: str
    :param days: Quantidade de dias para adicionar (positivo) ou subtrair (negativo).
    :type days: int
    :return: A nova data após adicionar/subtrair a quantidade especificada de dias no formato yyyy-mm-dd.
    :rtype: str
    """
    new_date = datetime.strptime(date, '%Y-%m-%d') + timedelta(int(days))
    return new_date.astimezone().strftime('%Y-%m-%d')


def generate_randon_date(date_format: Literal["yyyy-mm-dd", "yyyy-mm"] = "yyyy-mm-dd") -> str:
    """
    Gera uma data aleatória.

    :return: Uma data aleatória no formato yyyy-mm-dd ou yyy-mm.
    :rtype: str
    """
    if date_format not in ["yyyy-mm-dd", "yyyy-mm"]:
        raise Exception('Invalid "date_format". Allowed: "yyyy-mm-dd" or "yyyy-mm".')
    new_date_format = "%Y-%m-%d" if date_format == "yyyy-mm-dd" else "%Y-%m"
    new_date = '{}-{:02d}-{:02d}'.format(choice(range(2024, 2100)), choice(range(1, 13)), choice(range(1, 28)))
    
    return datetime.strptime(new_date, '%Y-%m-%d').strftime(new_date_format)
