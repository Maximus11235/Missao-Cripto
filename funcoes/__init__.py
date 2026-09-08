# funcoes/__init__.py

# O ponto (.) antes de 'max' significa "procure no mesmo diretório deste __init__.py"
from .max import euclides_estendido, inverso_multiplicativo, eh_primo

from .Andressa import (
    congruencia_linear,
    inverso_modular,
    mdc,
    mdc_recursivo,
    mod,
    mult_mod,
    pot_mod,
    sao_coprimos,
    soma_mod,
    sub_mod,
    totiente_euler,
)

__all__ = [
    "congruencia_linear",
    "eh_primo",
    "euclides_estendido",
    "inverso_multiplicativo",
    "inverso_modular",
    "mdc",
    "mdc_recursivo",
    "mod",
    "mult_mod",
    "pot_mod",
    "sao_coprimos",
    "soma_mod",
    "sub_mod",
    "totiente_euler",
]
