from .max import inverso_multiplicativo

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
        inverso_parcial = inverso_multiplicativo(modulo_parcial, modulo_atual)

        # Acumula a parcela da solução com base no resto, módulo parcial e inverso
        soma_total += resto_atual * modulo_parcial * inverso_parcial

    # O resultado final é o resto da divisão pelo módulo total
    return soma_total % modulo_total

def multiplicar_matriz(A, B, modulo=None):
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])

    if colunas_A != linhas_B:
        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B.")

    resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            soma = sum(A[i][k] * B[k][j] for k in range(colunas_A))
            resultado[i][j] = soma % modulo if modulo else soma

    return resultado


def determinante(matriz):
    n = len(matriz)
    
    # Casos base para otimização
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])

    det = 0
    for c in range(n):
        # Cria a submatriz ignorando a linha 0 e a coluna c
        submatriz = [linha[:c] + linha[c+1:] for linha in matriz[1:]]
        sinal = (-1) ** c
        det += sinal * matriz[0][c] * determinante(submatriz)
        
    return det


def adjunta(matriz):
    n = len(matriz)
    if n == 1:
        return [[1]]
        
    cofatores = []
    for i in range(n):
        linha_cofatores = []
        for j in range(n):
            # Cria a submatriz removendo a linha i e a coluna j
            submatriz = [linha[:j] + linha[j+1:] for k, linha in enumerate(matriz) if k != i]
            sinal = (-1) ** (i + j)
            linha_cofatores.append(sinal * determinante(submatriz))
        cofatores.append(linha_cofatores)
        
    # A adjunta é a transposta da matriz de cofatores
    matriz_adjunta = [[cofatores[j][i] for j in range(n)] for i in range(n)]
    
    return matriz_adjunta
