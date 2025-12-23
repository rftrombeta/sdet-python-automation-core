import random


def generate_account(caracteres=8):
    """
    Gera um valor para Account de acordo com a quantidade de caracteres. O valor padrão é 8.

    Parameters
    ----------
    caracteres: int, optional
        Quantidade de caracteres para o Account. O valor padrão é 8.

    Returns
    -------
    str
        Valor numérico aleatório para ser utilizado como Account.
    """
    return ''.join(str(random.randrange(0, 9)) for _ in range(caracteres))
