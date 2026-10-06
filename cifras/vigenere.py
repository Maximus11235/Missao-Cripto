def cifrar(texto: str, chave: str) -> str:
    """
    Cifra uma mensagem utilizando a Cifra de Vigenère.
    Preserva maiúsculas, minúsculas, espaços e pontuações.
    """
    # Valida se a chave foi fornecida
    if not chave:
        raise ValueError("A chave não pode ser vazia.")

    # Filtra a chave mantendo apenas letras e convertendo para maiúsculas
    chave_limpa = [caractere.upper() for caractere in chave if caractere.isalpha()]
    if not chave_limpa:
        raise ValueError("A chave deve conter pelo menos uma letra do alfabeto.")

    resultado = []
    indice_chave = 0
    tamanho_chave = len(chave_limpa)

    # Percorre cada caractere da mensagem de texto
    for caractere in texto:
        # Se for uma letra (A-Z ou a-z), aplica a cifragem
        if caractere.isalpha():
            # Define o ponto de partida ASCII ('A' = 65 para maiúsculas, 'a' = 97 para minúsculas)
            base_ascii = ord('A') if caractere.isupper() else ord('a')
            
            # Converte a letra do texto para uma posição numérica no alfabeto (0 a 25)
            pos_texto = ord(caractere) - base_ascii
            
            # Obtém a letra atual da chave e descobre seu deslocamento (0 a 25)
            letra_chave = chave_limpa[indice_chave % tamanho_chave]
            deslocamento = ord(letra_chave) - ord('A')
            
            # Aplica a fórmula matemática de Vigenère: C_i = (P_i + K_i) mod 26
            nova_posicao = (pos_texto + deslocamento) % 26
            
            # Converte a nova posição de volta para o caractere correspondente mantendo a caixa (maiúscula/minúscula)
            resultado.append(chr(base_ascii + nova_posicao))
            
            # Avança o índice da chave APENAS quando processar uma letra
            indice_chave += 1
        else:
            # Mantém intactos espaços, números, pontuações e símbolos
            resultado.append(caractere)

    # Junta a lista de caracteres em uma string final
    return "".join(resultado)


def decifrar(texto: str, chave: str) -> str:
    """
    Decifra uma mensagem cifrada com a Cifra de Vigenère.
    Preserva maiúsculas, minúsculas, espaços e pontuações.
    """
    # Valida se a chave foi fornecida
    if not chave:
        raise ValueError("A chave não pode ser vazia.")

    # Filtra a chave mantendo apenas letras em maiúsculas
    chave_limpa = [caractere.upper() for caractere in chave if caractere.isalpha()]
    if not chave_limpa:
        raise ValueError("A chave deve conter pelo menos uma letra do alfabeto.")

    resultado = []
    indice_chave = 0
    tamanho_chave = len(chave_limpa)

    # Percorre cada caractere da mensagem cifrada
    for caractere in texto:
        # Se for uma letra, aplica a decifragem
        if caractere.isalpha():
            # Define o ponto de partida ASCII ('A' ou 'a')
            base_ascii = ord('A') if caractere.isupper() else ord('a')
            
            # Converte a letra cifrada para uma posição numérica no alfabeto (0 a 25)
            pos_cifrada = ord(caractere) - base_ascii
            
            # Obtém o deslocamento da chave atual (0 a 25)
            letra_chave = chave_limpa[indice_chave % tamanho_chave]
            deslocamento = ord(letra_chave) - ord('A')
            
            # Aplica a fórmula inversa de Vigenère: P_i = (C_i - K_i) mod 26
            # O operador % 26 no Python lida perfeitamente com resultados negativos
            nova_posicao = (pos_cifrada - deslocamento) % 26
            
            # Converte de volta para caractere mantendo a caixa original
            resultado.append(chr(base_ascii + nova_posicao))
            
            # Avança o índice da chave apenas ao processar letras
            indice_chave += 1
        else:
            # Mantém espaços e caracteres especiais intactos
            resultado.append(caractere)

    # Junta a lista de caracteres em uma string final
    return "".join(resultado)