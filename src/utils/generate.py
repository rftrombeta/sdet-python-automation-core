import random
import string


def random_string(length=12, chars=None, prefix='', suffix='', exclude_ambiguous=False):
    """
    Gera uma string aleatória.

    Parameters
    ----------
    length : int, optional
        Comprimento da parte aleatória da string (padrão: 12).
    chars : str or None, optional
        Conjunto de caracteres a serem usados. Se None, usa letras ASCII (maiúsculas e minúsculas) e dígitos.
    prefix : str, optional
        Texto a ser prefixado à string gerada.
    suffix : str, optional
        Texto a ser sufixado à string gerada.
    exclude_ambiguous : bool, optional
        Se True, remove caracteres ambíguos como '0', 'O', '1', 'l', 'I'.

    Returns
    -------
    str
        String aleatória gerada.
    """
    if length < 0:
        raise ValueError("length must be non-negative")
    if chars is None:
        chars = string.ascii_letters + string.digits
    if exclude_ambiguous:
        ambiguous = set('0O1lI')
        chars = ''.join(c for c in chars if c not in ambiguous)
    return prefix + ''.join(random.choice(chars) for _ in range(length)) + suffix


def random_alphanumeric(length=12, **kwargs):
    """Alias para gerar strings alfanuméricas."""
    return random_string(length=length, chars=string.ascii_letters + string.digits, **kwargs)


def random_numeric(length=6, **kwargs):
    """Gera uma string contendo apenas dígitos."""
    return random_string(length=length, chars=string.digits, **kwargs)


def random_lowercase(length=8, **kwargs):
    """Gera uma string contendo apenas letras minúsculas."""
    return random_string(length=length, chars=string.ascii_lowercase, **kwargs)
