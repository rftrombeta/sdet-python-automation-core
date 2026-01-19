"""
SDET Python Automation Core

Biblioteca compartilhada para automação de testes com models Pydantic,
geradores de dados e utilitários.
"""

from . import generators
from . import models
from . import url
from . import utils

__version__ = "0.1.0"

__all__ = [
    "generators",
    "models",
    "url",
    "utils",
    "__version__",
]
