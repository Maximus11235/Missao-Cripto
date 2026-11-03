import sys
import os

# Adiciona a raiz do projeto ao sys.path para importação do pacote 'cifras'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from missao3 import (
    cifrar_des_ecb, decifrar_des_ecb,
    cifrar_des_cbc, decifrar_des_cbc,
    cifrar_des_cfb, decifrar_des_cfb,
    cifrar_des_ofb, decifrar_des_ofb,
)

# Chave (64 bits) e Vetor de Inicialização IV (64 bits)
CHAVE = "0000000100100011010001010110011110001001101010111100110111101111"
IV    = "1111111100000000111111110000000011111111000000001111111100000000"
TEXTO = "0100100001101111011011000110000101001101011101010110111001100100"

def imprimir_resultado_modo(nome_modo, original, cifrado, decifrado):
    print(f"\n--- MODO {nome_modo} ---")
    print(f"Mensagem Inicial:  {original}")
    print(f"Mensagem Cifrada:  {cifrado}")
    print(f"Texto Decifrado:   {decifrado}")
    assert original == decifrado, f"Erro: Decifragem falhou no modo {nome_modo}!"
    print(f"Resultado:         [OK] Decifragem idêntica ao texto inicial.")

def executar_testes():
    print("================ EXECUÇÃO COMPLETA DO DES ================")
    
    # Modo ECB
    cifra_ecb = cifrar_des_ecb(TEXTO, CHAVE)
    decifrado_ecb = decifrar_des_ecb(cifra_ecb, CHAVE)
    imprimir_resultado_modo("ECB", TEXTO, cifra_ecb, decifrado_ecb)
    
    # Modo CBC
    cifra_cbc = cifrar_des_cbc(TEXTO, CHAVE, IV)
    decifrado_cbc = decifrar_des_cbc(cifra_cbc, CHAVE, IV)
    imprimir_resultado_modo("CBC", TEXTO, cifra_cbc, decifrado_cbc)
    
    # Modo CFB
    cifra_cfb = cifrar_des_cfb(TEXTO, CHAVE, IV)
    decifrado_cfb = decifrar_des_cfb(cifra_cfb, CHAVE, IV)
    imprimir_resultado_modo("CFB", TEXTO, cifra_cfb, decifrado_cfb)
    
    # Modo OFB
    cifra_ofb = cifrar_des_ofb(TEXTO, CHAVE, IV)
    decifrado_ofb = decifrar_des_ofb(cifra_ofb, CHAVE, IV)
    imprimir_resultado_modo("OFB", TEXTO, cifra_ofb, decifrado_ofb)
    
    print("\n==========================================================")

if __name__ == "__main__":
    executar_testes()