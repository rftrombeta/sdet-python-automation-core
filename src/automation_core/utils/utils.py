from datetime import datetime
from pytz import timezone
import json
import os
import re

path = os.getcwd()
base_path = f"{path}/src/utils/" if "qa-libs-auto-api" in path else f"{path}/utils/"

def get_hour_now():
    """
    Obtém a hora atual para inserir no relatório do slack.

    Returns
    -------
    str
        Retorna a hora atual no formato HH:MM:SS.
    """
    return datetime.now().astimezone(timezone('Etc/GMT+3')).strftime('%H:%M:%S')


def convert_response_json(response):
    """
    Recebe um response formatado com apóstrofo para conversão em json.

    Parameters
    ----------
    response: str
        Response da request.

    Returns
    -------
    dict
        Response no formato json.
    """
    return json.loads(response, strict=False)


def replace_string_patterns(string_original, pattern, replacement):
    """
    Substitui uma correspondência de expressão regular.

    Parameters
    ----------
    string_original: str
        String contendo a expressão que será alterada.
    pattern: str
        Expressão que será localizada na string para substituição.
    replacement: str
        Expressão que substituirá o pattern.

    Returns
    -------
    str
        Nova string após substituição da expressão regular.
    """
    return re.sub(pattern, replacement, json.dumps(string_original))


def force_known_error_message(task_azure):
    """
    Indica que o teste possui um erro que já é conhecido e que o mesmo já possui um card aberto.

    Parameters
    ----------
    task_azure: str
        Número da task aberta no Azure para tratar o erro.

    Returns
    -------
    None
    """
    raise Exception(f'Esse teste falha e é um bug conhecido! ({task_azure}).')
