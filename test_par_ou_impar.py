import pytest
from par_ou_impar import verificar_numero


@pytest.mark.parametrize("numero, resultado",[
        (2, "Par"),
        (3, "Impar"),
        (4, "Par"),
        (5, "Impar"),
        (10, "Par"),
        (7, "Impar"),
        (0, "Par"),
        (-2, "Par"),
        (-3, "Impar"),
    ],
)
def test_verificar_numero(numero, resultado):
    assert verificar_numero(numero) == resultado