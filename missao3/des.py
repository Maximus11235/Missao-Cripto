# cifras/des.py

# ==========================================
# TABELAS DE PERMUTAÇÃO E SUBSTITUIÇÃO
# ==========================================

# Permutação Inicial (IP) e Inversa (IP_INVERSO)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

IP_INVERSO= [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

# Expansão (E) e Permutação (P) da Função F
E_BOX = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

P_BOX = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

# Geração de Chaves (PC-1 e PC-2)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Caixas S (S1 a S8)
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


# ==========================================
# MÓDULO 1: OPERAÇÕES BÁSICAS
# ==========================================

def aplicar_permutacao(bloco, tabela):
    """Permuta os bits de acordo com a tabela especificada (1-based index)."""
    return "".join(bloco[i - 1] for i in tabela)

def deslocamento_circular(bits, n):
    """Desloca a string de bits para a esquerda em n posições."""
    return bits[n:] + bits[:n]

def operacao_xor(bits_a, bits_b):
    """Realiza XOR entre duas strings binárias de mesmo tamanho."""
    return "".join('1' if a != b else '0' for a, b in zip(bits_a, bits_b))

def formatar_binario(inteiro, tamanho):
    """Converte inteiro para binário fixo (ex: 4 para '0100')."""
    return bin(inteiro)[2:].zfill(tamanho)


# ==========================================
# MÓDULO 2: GERAÇÃO DE CHAVES
# ==========================================

def gerar_subchaves(chave_64bits):
    """Gera 16 subchaves de 48 bits a partir da chave de 64 bits."""
    chave_56bits = aplicar_permutacao(chave_64bits, PC1)
    C, D = chave_56bits[:28], chave_56bits[28:]
    subchaves = []
    
    for shift in SHIFTS:
        C = deslocamento_circular(C, shift)
        D = deslocamento_circular(D, shift)
        subchaves.append(aplicar_permutacao(C + D, PC2))
        
    return subchaves


# ==========================================
# MÓDULO 3: O NÚCLEO DO DES (1 Bloco)
# ==========================================

def funcao_f(R, subchave):
    """Função F: Expansão, XOR com chave, Caixas S e Permutação P."""
    R_expandido = aplicar_permutacao(R, E_BOX)
    bloco_xor = operacao_xor(R_expandido, subchave)
    
    saida_sbox = ""
    for i in range(8):
        fragmento = bloco_xor[i*6 : (i+1)*6]
        linha = int(fragmento[0] + fragmento[5], 2)
        coluna = int(fragmento[1:5], 2)
        valor = S_BOXES[i][linha][coluna]
        saida_sbox += formatar_binario(valor, 4)
        
    return aplicar_permutacao(saida_sbox, P_BOX)

def processar_bloco_64bits(bloco, chave, decifrar=False):
    """Processa um bloco único de 64 bits pelas 16 rodadas da Rede de Feistel."""
    subchaves = gerar_subchaves(chave)
    if decifrar:
        subchaves.reverse()
        
    bloco_ip = aplicar_permutacao(bloco, IP)
    L, R = bloco_ip[:32], bloco_ip[32:]
    
    for i in range(16):
        L_novo = R
        R_novo = operacao_xor(L, funcao_f(R, subchaves[i]))
        L, R = L_novo, R_novo
        
    bloco_final = R + L  # Inversão final (swap)
    return aplicar_permutacao(bloco_final, IP_INVERSO)


# ==========================================
# MÓDULO 4: MODOS DE OPERAÇÃO
# ==========================================

def padronizar_texto(texto):
    """Preenche com '0's até ser múltiplo de 64."""
    faltam = 64 - (len(texto) % 64)
    if faltam == 64: return texto
    return texto + ('0' * faltam)

def fragmentar(texto):
    return [texto[i:i+64] for i in range(0, len(texto), 64)]

def cifrar_ecb(texto_bin, chave_bin):
    """Eletronic Codebook - Cifra cada bloco independentemente."""
    texto_bin = padronizar_texto(texto_bin)
    blocos = fragmentar(texto_bin)
    return "".join(processar_bloco_64bits(b, chave_bin) for b in blocos)

def decifrar_ecb(cifra_bin, chave_bin):
    blocos = fragmentar(cifra_bin)
    return "".join(processar_bloco_64bits(b, chave_bin, decifrar=True) for b in blocos)

def cifrar_cbc(texto_bin, chave_bin, iv_bin):
    """Cipher Block Chaining - XOR com bloco anterior antes de cifrar."""
    texto_bin = padronizar_texto(texto_bin)
    blocos = fragmentar(texto_bin)
    cifra_final = ""
    bloco_anterior = iv_bin
    
    for bloco in blocos:
        bloco_xor = operacao_xor(bloco, bloco_anterior)
        cifrado = processar_bloco_64bits(bloco_xor, chave_bin)
        cifra_final += cifrado
        bloco_anterior = cifrado
        
    return cifra_final

def decifrar_cbc(cifra_bin, chave_bin, iv_bin):
    blocos = fragmentar(cifra_bin)
    texto_final = ""
    bloco_anterior = iv_bin
    
    for bloco in blocos:
        decifrado = processar_bloco_64bits(bloco, chave_bin, decifrar=True)
        texto_final += operacao_xor(decifrado, bloco_anterior)
        bloco_anterior = bloco
        
    return texto_final

def cifrar_cfb(texto_bin, chave_bin, iv_bin):
    """Cipher Feedback - Cifra o retroalimentador e faz XOR com o texto."""
    texto_bin = padronizar_texto(texto_bin)
    blocos = fragmentar(texto_bin)
    cifra_final = ""
    registro = iv_bin
    
    for bloco in blocos:
        cifrado_registro = processar_bloco_64bits(registro, chave_bin)
        cifrado_bloco = operacao_xor(bloco, cifrado_registro)
        cifra_final += cifrado_bloco
        registro = cifrado_bloco
        
    return cifra_final

def decifrar_cfb(cifra_bin, chave_bin, iv_bin):
    """No CFB, a decifragem usa a operação de *cifragem* do algoritmo base."""
    blocos = fragmentar(cifra_bin)
    texto_final = ""
    registro = iv_bin
    
    for bloco in blocos:
        cifrado_registro = processar_bloco_64bits(registro, chave_bin) # Usa cifragem!
        texto_bloco = operacao_xor(bloco, cifrado_registro)
        texto_final += texto_bloco
        registro = bloco
        
    return texto_final

def cifrar_ofb(texto_bin, chave_bin, iv_bin):
    """Output Feedback - Gera fluxo contínuo de chaves independentes do texto."""
    texto_bin = padronizar_texto(texto_bin)
    blocos = fragmentar(texto_bin)
    cifra_final = ""
    registro = iv_bin
    
    for bloco in blocos:
        registro = processar_bloco_64bits(registro, chave_bin)
        cifra_final += operacao_xor(bloco, registro)
        
    return cifra_final

def decifrar_ofb(cifra_bin, chave_bin, iv_bin):
    """No OFB, cifrar e decifrar são operações idênticas."""
    return cifrar_ofb(cifra_bin, chave_bin, iv_bin)