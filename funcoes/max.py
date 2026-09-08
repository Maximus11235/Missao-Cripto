import math
def euclides_estendido(a, b):
    # Configuração inicial
    x_ant, x_atual = 1, 0
    y_ant, y_atual = 0, 1
    
    # O motor do algoritmo (a "caixa preta")
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x_ant, x_atual = x_atual, x_ant - q * x_atual
        y_ant, y_atual = y_atual, y_ant - q * y_atual
        
    # Retorna o MDC e os dois coeficientes
    return a, x_ant, y_ant


# 2. A nova função do Inverso Multiplicativo
def inverso_multiplicativo(a, m):
    """
    Calcula o inverso multiplicativo de 'a' no módulo 'm'.
    Retorna o inverso, ou None se o inverso não existir.
    """
    # Usamos nossa "caixa preta" passando o número e o módulo
    mdc, x, y = euclides_estendido(a, m)
    
    # Regra matemática: O inverso SÓ EXISTE se o MDC for exatamente 1
    if mdc != 1:
        print(f"O inverso de {a} mod {m} não existe (MDC não é 1).")
        return None
        
    # O Python já lida bem com números negativos no operador de resto (%),
    # então isso garante que a resposta será positiva e dentro do limite de 'm'.
    inverso = x % m
    
    return inverso




def eh_primo(n):
    """
    Verifica se um número 'n' é primo.
    Retorna True (Verdadeiro) se for primo, ou False (Falso) se não for.
    """
    # 0, 1 e números negativos não são primos
    if n <= 1:
        return False
        
    # 2 é o único número primo par
    if n == 2:
        return True
        
    # Se for par e maior que 2, já sabemos que não é primo
    if n % 2 == 0:
        return False
        
    # Testa os divisores ímpares começando do 3 até a raiz quadrada de 'n'
    limite = math.isqrt(n) # math.isqrt calcula a raiz quadrada exata
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False # Se dividiu e deu resto zero, não é primo
            
    # Se passou por todos os testes e não encontrou divisores, ele é primo
    return True