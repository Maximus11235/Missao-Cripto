import random
import string

ALFABETO = string.ascii_uppercase


def validar_chave(chave):
    chave = chave.upper()
    if len(chave) != 26 or set(chave) != set(ALFABETO):
        raise ValueError("A chave deve ser uma permutação das 26 letras do alfabeto")
    return chave


def gerar_chave(semente=None):
    letras = list(ALFABETO)
    random.Random(semente).shuffle(letras)
    return "".join(letras)


def chave_por_palavra(palavra):
    vistas = []
    for c in palavra.upper():
        if c in ALFABETO and c not in vistas:
            vistas.append(c)
    resto = [c for c in ALFABETO if c not in vistas]
    return "".join(vistas + resto)


def _traduzir(texto, origem, destino):
    tabela = {}
    for o, d in zip(origem, destino):
        tabela[o] = d
        tabela[o.lower()] = d.lower()
    return "".join(tabela.get(c, c) for c in texto)


def cifrar(texto, chave):
    chave = validar_chave(chave)
    return _traduzir(texto, ALFABETO, chave)


def decifrar(texto, chave):
    chave = validar_chave(chave)
    return _traduzir(texto, chave, ALFABETO)


def inverter_chave(chave):
    chave = validar_chave(chave)
    inv = [""] * 26
    for i, c in enumerate(chave):
        inv[ALFABETO.index(c)] = ALFABETO[i]
    return "".join(inv)


def analise_frequencia(texto):
    contagem = {c: 0 for c in ALFABETO}
    total = 0
    for c in texto.upper():
        if c in contagem:
            contagem[c] += 1
            total += 1
    if total == 0:
        return {c: 0.0 for c in ALFABETO}
    return {c: contagem[c] / total for c in ALFABETO}


def espaco_de_chaves():
    resultado = 1
    for i in range(2, 27):
        resultado *= i
    return resultado


if __name__ == "__main__":
    mensagem = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
    chave = chave_por_palavra("SEGURANCA")
    cifrado = cifrar(mensagem, chave)
    claro = decifrar(cifrado, chave)
    assert claro == mensagem
    assert decifrar(cifrar("Olá, Mundo!", chave), chave) == "Olá, Mundo!"
    assert decifrar(cifrado, inverter_chave(inverter_chave(chave))) == mensagem
    aleatoria = gerar_chave(42)
    assert decifrar(cifrar(mensagem, aleatoria), aleatoria) == mensagem
    print("Chave:", chave)
    print("Cifrado:", cifrado)
    print("Decifrado:", claro)
    print("Espaço de chaves:", espaco_de_chaves())
