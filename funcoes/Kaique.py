def calcularPhi(numero: int) -> int:

    if numero <= 0:
        raise ValueError("O número deve ser um inteiro positivo maior que zero.")
        
    resultado = numero
    fator = 3

    # Remove o fator primo 2 e atualiza o resultado
    if numero % 2 == 0:
        resultado -= (resultado // 2)
        while numero % 2 == 0:
            numero //= 2

    # Verifica os fatores primos ímpares a partir de 3
    while fator * fator <= numero:
        if numero % fator == 0:
            resultado -= (resultado // fator)
            while numero % fator == 0:
                numero //= fator           
        fator += 2

    # Se restar um fator primo maior que a raiz do numero
    if numero > 1:
        resultado -= resultado // numero
        
    return resultado

# Entrada de dados
n = int(input())
print(calcularPhi(n))


def expModular(base: int, exp: int, mod: int) -> int:

    resultado = 1
    
    while exp != 0:
        if exp % 2 == 0:
            # Se o expoente for par: eleva a base ao quadrado e divide o expoente por 2
            exp //= 2
            base = (base * base) % mod
        else:
            # Se o expoente for ímpar: multiplica o resultado pela base atual e reduz o expoente
            resultado = (resultado * base) % mod
            exp -= 1

    return resultado

def teoremaChinesResto(lista_restos: list, lista_modulos: list) -> int:

    # Calcula o produto de todos os módulos
    modulo_total = 1
    for modulo in lista_modulos:
        modulo_total *= modulo

    soma_total = 0
    # Processa cada congruência do sistema
    for indice in range(len(lista_restos)):
        resto_atual = lista_restos[indice]
        modulo_atual = lista_modulos[indice]
        
        # Calcula o módulo parcial (produto total dividido pelo módulo atual)
        modulo_parcial = modulo_total // modulo_atual

        # Encontra o inverso modular do módulo parcial em relação ao módulo atual
        inverso_parcial = inversoModular(modulo_parcial, modulo_atual)

        # Acumula a parcela da solução com base no resto, módulo parcial e inverso
        soma_total += resto_atual * modulo_parcial * inverso_parcial

    # O resultado final é o resto da divisão pelo módulo total
    return soma_total % modulo_total