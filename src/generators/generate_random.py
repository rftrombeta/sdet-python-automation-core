import random
import string
import uuid


def generate_identifier_code_random(quantidade=6):
    """
    Gera um código identificador aleatório composto por dígitos.

    Parameters
    ----------
    quantidade: int, opcional
        O número de dígitos no código identificador. O padrão é 6.

    Returns
    -------
    str
        Uma string de dígitos aleatórios do comprimento especificado.
    """
    return ''.join(str(random.randint(0, 9)) for _ in range(quantidade))


def generate_identifier_reference(descryption=""):
    """
    Gera uma sequência alfanumérica com uma descrição especificada.

    Parameters
    ----------
    descryption: str, opcional
        A palavra a ser incluída no identificador.

    Returns
    -------
    str
        Uma sequência alfanumérica com a palavra "ROBOT-" como prefixo.
    """
    result_str = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    result_num = random.randint(1000, 9999)
    return f"{descryption}ROBOT-{str(result_num)}-{result_str}"


def generate_num_ref():
    """
    Gera uma sequência de inteiros de 32 bits aleatória.

    Returns
    -------
    str
        Uma representação em string de um inteiro de 32 bits aleatório.
    """
    return str(random.getrandbits(32))


def generate_uuid4():
    """
    Gera um identificador único universal (UUID) de 128 bits.

    Returns
    -------
    str
        Uma representação em string de um UUID.
    """
    return str(uuid.uuid4())
