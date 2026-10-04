from funcoes import multiplicar_matriz, determinante, adjunta, inverso_modular

def preparar_texto(texto, tamanho_bloco):
    texto = texto.upper().replace(" ", "")   
    # Preenche com o último caractere da mensagem até que seja múltiplo do tamanho da matriz
    if texto:
        ultimo_char = texto[-1]
        while len(texto) % tamanho_bloco != 0:
            texto += ultimo_char
            
    return [ord(c) - 65 for c in texto]

def matriz_inversa_chave(chave, modulo=26):
    n = len(chave)
    det = determinante(chave) % modulo   
    try:
        inv_det = inverso_modular(det, modulo)
    except Exception:
        raise ValueError(f"A matriz chave não é invertível no módulo {modulo}. Escolha outra chave.")
    
    adj = adjunta(chave)  

    # Multiplica a matriz adjunta pelo inverso modular do determinante
    inversa = [[(adj[i][j] * inv_det) % modulo for j in range(n)] for i in range(n)]
    return inversa

def encription_hill(texto_claro, chave):
    tamanho_bloco = len(chave)
    numeros = preparar_texto(texto_claro, tamanho_bloco)
    texto_cifrado = ""
    
    for i in range(0, len(numeros), tamanho_bloco):
        # Cria um vetor coluna para o bloco atual
        bloco = [[num] for num in numeros[i:i+tamanho_bloco]]
        
        # Multiplica a matriz chave pelo bloco em mod 26
        resultado = multiplicar_matriz(chave, bloco, modulo=26)
        
        for j in range(tamanho_bloco):
            texto_cifrado += chr(resultado[j][0] + 65)
            
    return texto_cifrado

def decription_hill(texto_cifrado, chave):
    tamanho_bloco = len(chave)
    inversa = matriz_inversa_chave(chave, modulo=26)
    
    # Textos cifrados da Cifra de Hill já devem ser múltiplos do bloco, não precisa de padding
    numeros = [ord(c) - 65 for c in texto_cifrado]
    texto_claro = ""
    
    for i in range(0, len(numeros), tamanho_bloco):
        bloco = [[num] for num in numeros[i:i+tamanho_bloco]]
        
        resultado = multiplicar_matriz(inversa, bloco, modulo=26)
        
        for j in range(tamanho_bloco):
            texto_claro += chr(resultado[j][0] + 65)
            
    return texto_claro