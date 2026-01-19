from ..utils import utils
from urllib.parse import urlparse
import os
from typing import Optional


def get_url_api() -> str:
    """
    Consulta a URL conforme ambiente em execução.

    Returns
    -------
    str
        URL correspondente ao ambiente.
    """
    return "https://serverest.dev/#/"
