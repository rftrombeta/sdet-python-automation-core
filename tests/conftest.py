"""
Configuração compartilhada para testes pytest.
"""

import pytest
from faker import Faker


@pytest.fixture
def fake():
    """Fixture para instância do Faker."""
    return Faker('pt_BR')
