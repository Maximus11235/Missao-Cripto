# tests/testes.py

# Veja como a importação fica limpa!
from funcoes import (eh_primo, inverso_multiplicativo, euclides_estendido,
mdc, calcularPhi, expModular)

print("Testando a biblioteca:")

# Testando a função de número primo
print("103 é primo?", eh_primo(103))

# Testando o inverso multiplicativo
print("Inverso de 3 mod 11:", inverso_multiplicativo(3, 11))

# Testando o MDC
print("MDC de 48 e 18:", MDC(48, 18))

# Testando a função calcularPhi
print("Phi de 10:", calcularPhi(10))

# Testando a exponenciação modular
print("Exponenciação de 5^3 mod 13:", expModular(5, 3, 13))

# Testando o teorema chinês do resto (ex: x ≡ 2 mod 3 e x ≡ 3 mod 5)
print("Teorema Chinês do Resto:", teoremaChinesResto([2, 3], [3, 5]))
