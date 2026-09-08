# Funções auxiliares de aritmética modular


# Aritmética modular
def mod(a, n):
    # Retorna o resto de a na divisão por n
    return a % n


# Soma módulo n
def soma_mod(a, b, n):
    # Soma a e b, depois aplica o módulo n
    return (a + b) % n


# Subtração módulo n
def sub_mod(a, b, n):
    # Subtrai b de a, depois aplica o módulo n
    return (a - b) % n


# Multiplicação módulo n
def mult_mod(a, b, n):
    # Multiplica a por b, depois aplica o módulo n
    return (a * b) % n


# Exponenciação módulo n
def pot_mod(base, exp, n):
    # Calcula base elevado a exp, módulo n, de forma eficiente
    return pow(base, exp, n)


# MDC pelo algoritmo de Euclides iterativo
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# MDC pelo algoritmo de Euclides recursivo
def mdc_recursivo(a, b):
    if b == 0:
        return abs(a)
    return mdc_recursivo(b, a % b)


# Algoritmo de Euclides estendido
def euclides_estendido(a, b):
    if b == 0:
        sinal = -1 if a < 0 else 1
        return abs(a), sinal, 0

    mdc_val, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return mdc_val, x, y


# Inverso modular pelo algoritmo de Euclides estendido
def inverso_modular(a, n):
    if n <= 1:
        raise ValueError("O módulo deve ser maior que 1")

    mdc_val, x, _ = euclides_estendido(a, n)
    if mdc_val != 1:
        raise ValueError(f"Inverso modular não existe para {a} mod {n}")
    return x % n


# Verificação de coprimalidade
def sao_coprimos(a, b):
    return mdc(a, b) == 1


# Teste de primalidade
def eh_primo(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# Totiente de Euler
def totiente_euler(n):
    if n <= 0:
        raise ValueError("n deve ser um inteiro positivo")

    resultado = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            resultado -= resultado // p
        p += 1
    if temp > 1:
        resultado -= resultado // temp
    return resultado


# Resolução de congruência linear
def congruencia_linear(a, b, n):
    if n <= 0:
        raise ValueError("O módulo deve ser um inteiro positivo")

    d = mdc(a, n)
    if b % d != 0:
        return []

    a1, b1, n1 = a // d, b // d, n // d
    x0 = (inverso_modular(a1, n1) * b1) % n1 if n1 > 1 else 0
    return [(x0 + i * n1) % n for i in range(d)]
