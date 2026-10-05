from math import gcd


def cifrar(texto, a, b):
    # Garante que a chave permita recuperar a mensagem.
    if gcd(a, 26) != 1:
        raise ValueError("A chave a deve ser coprima de 26.")

    resultado = ""

    for letra in texto:
        # Aplica E(x) = (a * x + b) mod 26, preservando maiúsculas e minúsculas.
        if "A" <= letra <= "Z":
            resultado += chr((a * (ord(letra) - 65) + b) % 26 + 65)
        elif "a" <= letra <= "z":
            resultado += chr((a * (ord(letra) - 97) + b) % 26 + 97)
        else:
            # Mantém espaços, pontuação e caracteres fora de A–Z e a–z.
            resultado += letra

    return resultado


def decifrar(texto, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("A chave a deve ser coprima de 26.")

    # Calcula o inverso multiplicativo de a módulo 26.
    inverso = pow(a, -1, 26)
    resultado = ""

    for letra in texto:
        # Aplica D(y) = inverso * (y - b) mod 26.
        if "A" <= letra <= "Z":
            resultado += chr((inverso * (ord(letra) - 65 - b)) % 26 + 65)
        elif "a" <= letra <= "z":
            resultado += chr((inverso * (ord(letra) - 97 - b)) % 26 + 97)
        else:
            resultado += letra

    return resultado


if __name__ == "__main__":
    # Mensagem da atividade e chave a b escolhida para o exemplo.
    mensagem = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
    a = 5
    b = 8

    texto_cifrado = cifrar(mensagem, a, b)
    texto_decifrado = decifrar(texto_cifrado, a, b)

    print("Texto claro:", mensagem)
    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)