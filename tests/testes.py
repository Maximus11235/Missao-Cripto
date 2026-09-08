# tests/testes.py

# Veja como a importação fica limpa!
from funcoes import eh_primo, inverso_multiplicativo, euclides_estendido

print("Testando a biblioteca:")

# Testando a função de número primo
print("103 é primo?", eh_primo(103))

# Testando o inverso multiplicativo
print("Inverso de 3 mod 11:", inverso_multiplicativo(3, 11))