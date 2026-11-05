import os
import sys

# Adiciona a raiz do projeto ao sys.path para importação do pacote oficial 'missao3'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importação oficial através do pacote estruturado do grupo (__init__.py)
from missao3 import cifrar_aes_ecb, decifrar_aes_ecb


def executar_testes():
    print("================ EXECUÇÃO COMPLETA DO AES-128 ================")

    # 1. Definição dos nomes dos arquivos físicos do experimento
    nome_original = "original_teste_AES.txt"
    nome_cifrado = "cifrado_teste_AES.bin"
    nome_recuperado = "recuperado_teste_AES.txt"

    # 2. Criação do arquivo de texto de entrada
    with open(nome_original, "w", encoding="utf-8") as f:
        f.write("Olá meu nome é Ruben Noronha\n")
        
    chave_aes = os.urandom(16)  # Geração da chave segura de 128 bits aleatória
    print(f"Chave Utilizada (hex): {chave_aes.hex()}")

    # 3. Chamada das funções oficiais importadas do pacote do grupo (passando os 3 argumentos)
    cifrar_aes_ecb(nome_original, nome_cifrado, chave_aes)
    decifrar_aes_ecb(nome_cifrado, nome_recuperado, chave_aes)

    # 4. Validação e verificação dos bytes gerados no HD local
    with open(nome_original, "rb") as f:
        original_bytes = f.read()
    with open(nome_cifrado, "rb") as f:
        cifrado_bytes = f.read()
    with open(nome_recuperado, "rb") as f:
        recuperado_bytes = f.read()

    print("\n--- RELATÓRIO FINAL AES (ECB) ---")
    print(f"Mensagem Inicial:  {original_bytes.decode('utf-8').strip()}")
    print(f"Mensagem Cifrada:  {cifrado_bytes.hex()[:64]}...")
    print(f"Texto Decifrado:   {recuperado_bytes.decode('utf-8').strip()}")
    
    assert original_bytes == recuperado_bytes, "Erro: Decifragem falhou! Os arquivos são diferentes."
    print("Resultado:         [OK] Decifragem idêntica ao texto inicial por meio do pacote integrado.")
    print("==============================================================")


if __name__ == "__main__":
    executar_testes()
