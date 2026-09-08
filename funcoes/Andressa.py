"""Funções auxiliares de aritmética modular."""


def mod(a, n):
    """Retorna o resto de ``a`` na divisão por ``n``."""
    return a % n


def soma_mod(a, b, n):
    """Soma dois valores módulo ``n``."""
    return (a + b) % n


def sub_mod(a, b, n):
    """Subtrai dois valores módulo ``n``."""
    return (a - b) % n


def mult_mod(a, b, n):
    """Multiplica dois valores módulo ``n``."""
    return (a * b) % n


def pot_mod(base, exp, n):
    """Calcula uma potência módulo ``n`` de forma eficiente."""
    return pow(base, exp, n)


def mdc(a, b):
    """Calcula o MDC pelo algoritmo de Euclides iterativo."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def mdc_recursivo(a, b):
    """Calcula o MDC pelo algoritmo de Euclides recursivo."""
    if b == 0:
        return abs(a)
    return mdc_recursivo(b, a % b)


def euclides_estendido(a, b):
    """Retorna o MDC e os coeficientes da identidade de Bézout."""
    if b == 0:
        sinal = -1 if a < 0 else 1
        return abs(a), sinal, 0

    mdc_val, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return mdc_val, x, y


def inverso_modular(a, n):
    """Calcula o inverso de ``a`` módulo ``n``."""
    if n <= 1:
        raise ValueError("O módulo deve ser maior que 1")

    mdc_val, x, _ = euclides_estendido(a, n)
    if mdc_val != 1:
        raise ValueError(f"Inverso modular não existe para {a} mod {n}")
    return x % n


def sao_coprimos(a, b):
    """Informa se ``a`` e ``b`` são coprimos."""
    return mdc(a, b) == 1


def eh_primo(n):
    """Verifica por divisão de tentativa se ``n`` é primo."""
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


def totiente_euler(n):
    """Calcula a função totiente de Euler para um inteiro positivo."""
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


def congruencia_linear(a, b, n):
    """Resolve ``a*x = b (mod n)`` e retorna todas as soluções."""
    if n <= 0:
        raise ValueError("O módulo deve ser um inteiro positivo")

    d = mdc(a, n)
    if b % d != 0:
        return []

    a1, b1, n1 = a // d, b // d, n // d
    x0 = (inverso_modular(a1, n1) * b1) % n1 if n1 > 1 else 0
    return [(x0 + i * n1) % n for i in range(d)]
