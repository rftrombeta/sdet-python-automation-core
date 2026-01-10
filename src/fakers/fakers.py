import random
import string


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


def generate_email(local_length=8, domain=None, domain_list=None, allow_digits=True, allow_dots=False):
    """
    Gera um e-mail aleatório simples.

    Parameters
    ----------
    local_length : int, optional
        Quantidade de caracteres do local-part (padrão: 8).
    domain : str or None, optional
        Domínio a ser usado; se None, será escolhido aleatoriamente de `domain_list`.
    domain_list : list or None, optional
        Lista de domínios a escolher quando `domain` for None.
    allow_digits : bool, optional
        Permite dígitos no local-part (padrão: True).
    allow_dots : bool, optional
        Permite que o local-part inclua pontos ('.') entre os caracteres (padrão: False).

    Returns
    -------
    str
        Um e-mail aleatório válido básico.

    Examples
    --------
    >>> generate_email()
    'xk3hgf7q@example.com'
    >>> generate_email(local_length=5, domain='mydomain.test')
    'abc12@mydomain.test'
    """
    if local_length <= 0:
        raise ValueError("local_length must be positive")

    if domain is None:
        if not domain_list:
            domain_list = ["example.com", "test.com", "mail.com", "example.org", "example.net", "automation.com"]
        domain = random.choice(domain_list)

    chars = string.ascii_lowercase
    if allow_digits:
        chars += string.digits

    # opcionalmente insere pontos entre caracteres
    if allow_dots and local_length > 1:
        parts = []
        for _ in range(local_length):
            parts.append(random.choice(chars))
        # insere aleatoriamente alguns pontos (não no começo/fim)
        num_dots = random.randrange(0, max(1, local_length // 4))
        for _ in range(num_dots):
            pos = random.randrange(1, len(parts))
            parts.insert(pos, '.')
        local = ''.join(parts)
    else:
        local = ''.join(random.choice(chars) for _ in range(local_length))

    # garante lowercase
    local = local.lower()

    return f"{local}@{domain}"
