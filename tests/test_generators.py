"""
Testes para geradores de dados.
"""

from sdet_python_automation_core.generators.generate_cnpj_cpf import (
    generate_cpf,
    generate_cnpj,
)
from sdet_python_automation_core.generators.generate_random import (
    generate_identifier_code_random,
    generate_identifier_reference,
    generate_uuid4,
    generate_num_ref,
)
from sdet_python_automation_core.generators.generate_date import (
    generate_current_date,
    generate_date_plus_n_days,
)


def test_generate_cpf():
    """Testa geração de CPF válido."""
    cpf = generate_cpf()
    
    assert isinstance(cpf, str)
    assert len(cpf) == 11
    assert cpf.isdigit()


def test_generate_cnpj():
    """Testa geração de CNPJ válido."""
    cnpj = generate_cnpj()
    
    assert isinstance(cnpj, str)
    assert len(cnpj) == 14
    assert cnpj.isdigit()


def test_generate_identifier_code_random():
    """Testa geração de código identificador."""
    codigo = generate_identifier_code_random(6)
    
    assert isinstance(codigo, str)
    assert len(codigo) == 6
    assert codigo.isdigit()


def test_generate_identifier_reference():
    """Testa geração de referência alfanumérica."""
    referencia = generate_identifier_reference("TEST")
    
    assert isinstance(referencia, str)
    assert "TEST" in referencia
    assert "-" in referencia


def test_generate_uuid4():
    """Testa geração de UUID v4."""
    uuid = generate_uuid4()
    
    assert isinstance(uuid, str)
    assert len(uuid) == 36
    assert uuid.count("-") == 4


def test_generate_num_ref():
    """Testa geração de número de referência."""
    num_ref = generate_num_ref()
    
    assert isinstance(num_ref, str)
    assert num_ref.isdigit()
    assert len(num_ref) > 0


def test_generate_current_date():
    """Testa geração de data atual."""
    data = generate_current_date()
    
    assert isinstance(data, str)
    assert len(data) == 10  # yyyy-mm-dd
    assert data.count("-") == 2


def test_generate_date_plus_n_days():
    """Testa geração de data futura."""
    data = generate_date_plus_n_days(30)
    
    assert isinstance(data, str)
    assert len(data) == 10  # yyyy-mm-dd
    assert data.count("-") == 2
