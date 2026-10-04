def encription_cesar(cipher, shot):
    nova_mensagem = ""
    for i in cipher:

        # Verifica se o caractere é uma letra maiúscula
        if ord(i) >= 65 and ord(i) <= 90:
            # Aplica o deslocamento dentro do limite de mod26
            conta = (ord(i) - 65 + shot) % 26
            # Converte o número de volta para caractere e adiciona à mensagem
            nova_mensagem += chr(conta + 65)
            continue

        # Verifica se o caractere é uma letra minúscula
        if ord(i) >= 97 and ord(i) <= 122:
            # Aplica o deslocamento dentro do limite de mod26
            conta = (ord(i) - 97 + shot) % 26
            # Converte o número de volta para caractere e adiciona à mensagem
            nova_mensagem += chr(conta + 97)
            continue

        # Mantém espaços e números como estão
        if i == " " or i.isdigit():
            nova_mensagem += i

    return nova_mensagem 


def decription_cesar(cipher, shot):
    nova_mensagem = ""
    for i in cipher:

        # Aplica o deslocamento dentro do limite de mod26
        if ord(i) >= 65 and ord(i) <= 90:
            # Subtrai o deslocamento para voltar ao original
            conta = (ord(i) - 65 - shot) % 26
            nova_mensagem += chr(conta + 65)
            continue

        # Aplica o deslocamento dentro do limite de mod26
        if ord(i) >= 97 and ord(i) <= 122:
            # Subtrai o deslocamento para voltar ao original
            conta = (ord(i) - 97 - shot) % 26
            nova_mensagem += chr(conta + 97)
            continue
        
        # Mantém espaços e números inalterados na mensagem final
        if i == " " or i.isdigit():
            nova_mensagem += i

    return nova_mensagem

        
