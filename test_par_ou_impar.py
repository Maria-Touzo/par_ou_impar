import pytest
from par_ou_impar import verificar_numero

@pytest.mark.parametrize("numero", resultado [
    ("2", "Par"),
    ("3", "Ímpar"),
    ("4", "Par"),
    ("5", "Ímpar"),
    ("10", "Par"),
    ("7", "Ímpar"),
    ("0", "Par"),
    ("-2", "Par"),
    ("-3", "Ímpar"),
])

def test_verificar_numero(numero, resutado):
    assert verificar_numero(numero) == resutado

