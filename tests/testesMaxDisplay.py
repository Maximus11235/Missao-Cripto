import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path para evitar erros de importação de pacotes
sys.path.append(str(Path(__file__).resolve().parent.parent))
# if str(RAIZ_PROJETO) not in sys.path:
#     sys.path.append(str(RAIZ_PROJETO))

# Importação da cifra de Vigenère
from cifras.vigenere import cifrar as cifrar_vigenere, decifrar as decifrar_vigenere

# Tentativa de importação da cifra de transposição (será carregada assim que implementarmos)
try:
    from cifras.transposicao import cifrar as cifrar_transposicao, decifrar as decifrar_transposicao
    TRANSPOSICAO_DISPONIVEL = True
except ImportError:
    TRANSPOSICAO_DISPONIVEL = False


def cabecalho(titulo: str):
    """Exibe um cabeçalho formatado no terminal."""
    print("\n" + "=" * 60)
    print(f"{titulo.center(60)}")
    print("=" * 60)


def exibir_fluxo_vigenere():
    """Executa o teste interativo para a Cifra de Vigenère."""
    cabecalho("HUB DE TESTES: CIFRA DE VIGENÈRE")
    
    # Entrada de dados pelo usuário
    mensagem = input("\n[1] Digite a mensagem clara: ").strip()
    if not mensagem:
        print(">> Erro: A mensagem não pode estar vazia.")
        return

    chave = input("[2] Digite a palavra-chave: ").strip()
    if not chave:
        print(">> Erro: A chave não pode estar vazia.")
        return

    try:
        # Cifragem
        cifrado = cifrar_vigenere(mensagem, chave)
        
        # Decifragem
        decifrado = decifrar_vigenere(cifrado, chave)

        # Exibição do fluxo detalhado
        print("-" * 60)
        print(f" [+] Texto Original  : {mensagem}")
        print(f" [+] Chave Utilizada : {chave}")
        print(f" [+] Texto Cifrado   : {cifrado}")
        print(f" [+] Texto Decifrado : {decifrado}")
        print("-" * 60)
        # Por esta (remove os espaços de padding do final para comparar):
        if mensagem.rstrip(" ") == decifrado.rstrip(" "):
            print(" [STATUS]: REVERSIBILIDADE PERFEITA (Sucesso!)")
        else:
            print(" [STATUS]: FALHA NA REVERSIBILIDADE!")
    except ValueError as e:
        print(f">> Erro na execução: {e}")


def exibir_fluxo_transposicao():
    """Executa o teste interativo para a Cifra de Transposição."""
    cabecalho("HUB DE TESTES: CIFRA DE TRANSPOSIÇÃO")

    if not TRANSPOSICAO_DISPONIVEL:
        print("\n>> A Cifra de Transposição ainda não foi implementada em cifras/transposicao.py.")
        return

    mensagem = input("\n[1] Digite a mensagem clara: ").strip()
    chave = input("[2] Digite a palavra-chave para transposição: ").strip()

    try:
        cifrado = cifrar_transposicao(mensagem, chave)
        decifrado = decifrar_transposicao(cifrado, chave)

        print("-" * 60)
        print(f" [+] Texto Original  : {mensagem}")
        print(f" [+] Chave Utilizada : {chave}")
        print(f" [+] Texto Cifrado   : {cifrado}")
        print(f" [+] Texto Decifrado : {decifrado}")
        print("-" * 60)

        if mensagem == decifrado:
            print(" [STATUS]: REVERSIBILIDADE PERFEITA (Sucesso!)")
        else:
            print(" [STATUS]: FALHA NA REVERSIBILIDADE!")

    except Exception as e:
        print(f">> Erro na execução: {e}")


def exibir_fluxo_duplo():
    """Executa o teste em camada dupla: Vigenère + Transposição."""
    cabecalho("HUB DE TESTES: DUPLA CAMADA (VIGENÈRE + TRANSPOSIÇÃO)")

    if not TRANSPOSICAO_DISPONIVEL:
        print("\n>> Cifra de Transposição pendente. Implemente o arquivo transposicao.py primeiro.")
        return

    mensagem = input("\n[1] Digite a mensagem clara: ").strip()
    chave_vigenere = input("[2] Chave para Vigenère: ").strip()
    chave_transposicao = input("[3] Chave para Transposição: ").strip()

    try:
        # Cifragem em duas etapas
        etapa_1_cifrada = cifrar_vigenere(mensagem, chave_vigenere)
        etapa_2_cifrada = cifrar_transposicao(etapa_1_cifrada, chave_transposicao)

        # Decifragem na ordem inversa
        etapa_1_decifrada = decifrar_transposicao(etapa_2_cifrada, chave_transposicao)
        mensagem_final = decifrar_vigenere(etapa_1_decifrada, chave_vigenere)

        print("-" * 60)
        print(f" [0] Texto Original          : {mensagem}")
        print(f" [1] Após Cifra Vigenère     : {etapa_1_cifrada}")
        print(f" [2] Após Cifra Transposição : {etapa_2_cifrada}")
        print(" " + "." * 58)
        print(f" [3] Decifrado Transposição  : {etapa_1_decifrada}")
        print(f" [4] Decifrado Vigenère      : {mensagem_final}")
        print("-" * 60)

        if mensagem.rstrip(" ") == mensagem_final.rstrip(" "):
            print(" [STATUS]: DUPLA CRIPTOGRAFIA REVERTIDA COM SUCESSO!")
        else:
            print(" [STATUS]: FALHA NA REVERSIBILIDADE DA DUPLA CAMADA!")

    except Exception as e:
        print(f">> Erro na execução: {e}")


def main():
    """Menu principal do Hub de Testes Display."""
    while True:
        cabecalho("DISPLAY INTERATIVO DE TESTES - MISSÃO CRIPTO")
        print(" [1] Testar Cifra de Vigenère")
        print(" [2] Testar Cifra de Transposição")
        print(" [3] Testar Cifragem em Dupla Camada (Vigenère + Transposição)")
        print(" [0] Sair do Hub")
        print("=" * 60)

        opcao = input(" Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_fluxo_vigenere()
        elif opcao == "2":
            exibir_fluxo_transposicao()
        elif opcao == "3":
            exibir_fluxo_duplo()
        elif opcao == "0":
            print("\nEncerrando o Display de Testes. Até mais!\n")
            break
        else:
            print("\n>> Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()