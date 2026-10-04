import secrets
from cifras.cifra_fluxo import StreamCipher

def executar_teste():
    # Dados da Situação-Problema
    mensagem_interceptada = "SABIA QUE O SABIAH SABIA ASSOBIAR?".encode('utf-8')
    
    # Gera uma chave de 16 bytes (128 bits)
    chave_secreta = secrets.token_bytes(16)

    print("--- Teste da Cifra de Fluxo (RC4) com Chave Aleatória ---")
    print(f"Texto Claro Original: {mensagem_interceptada.decode('utf-8')}")
    print(f"Chave Aleatória Gerada (Hex): {chave_secreta.hex()}\n")

    # Cifragem (Simulando o envio pelo funcionário)
    cipher_encrypt = StreamCipher(chave_secreta)
    texto_cifrado = cipher_encrypt.process(mensagem_interceptada)
    
    print(f"Texto Cifrado (Interceptado na rede): {texto_cifrado.hex()}")

    # Decifragem (Simulando o recebimento pelo Servidor Central)
    # O servidor precisa receber a MESMA chave aleatória que foi usada na cifragem
    cipher_decrypt = StreamCipher(chave_secreta)
    texto_decifrado = cipher_decrypt.process(texto_cifrado)
    
    print(f"Texto Decifrado: {texto_decifrado.decode('utf-8')}")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    executar_teste()