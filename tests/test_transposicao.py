import sys
from pathlib import Path

# Adiciona a pasta raiz do projeto ao caminho de busca do Python para evitar ModuleNotFoundError
sys.path.append(str(Path(__file__).resolve().parent.parent))

import random
import string
import unittest
# Importa as funções de Transposição
from cifras.transposicao import cifrar, decifrar


class TestCifraTransposicaoDinamico(unittest.TestCase):

    def test_casos_estaticos_e_subtestes(self):
        """Testa diferentes frases e chaves garantindo a reversibilidade exata."""
        
        casos = [
            {"texto": "TRANSFERIR DOCUMENTO", "chave": "CHAVE", "desc": "Mensagem clássica com chave simples"},
            {"texto": "Ataque ao Amanhecer às 05h!", "chave": "SENHA", "desc": "Mensagem com números e pontuação"},
            {"texto": "Python Cripto 2026", "chave": "LIMAO", "desc": "Frase com números e espaços"},
            {"texto": "LetrasRepetidasNaChave", "chave": "BANANA", "desc": "Chave com letras repetidas (A e N)"},
        ]

        for caso in casos:
            with self.subTest(descricao=caso["desc"], texto=caso["texto"], chave=caso["chave"]):
                cifrado = cifrar(caso["texto"], caso["chave"])
                decifrado = decifrar(cifrado, caso["chave"])
                
                # Compara ignorando os espaços de padding adicionados ao final da mensagem
                self.assertEqual(decifrado.rstrip(" "), caso["texto"].rstrip(" "))

    def test_reversibilidade_com_dados_aleatorios(self):
        """Gera 100 mensagens e chaves aleatórias para testar a reversibilidade matemática."""
        
        for i in range(100):
            tamanho_texto = random.randint(10, 150)
            tamanho_chave = random.randint(2, 15)

            # Gera caracteres variados
            caracteres = string.ascii_letters + string.digits + " !?@#"
            texto_aleatorio = "".join(random.choice(caracteres) for _ in range(tamanho_texto))
            chave_aleatoria = "".join(random.choice(string.ascii_letters) for _ in range(tamanho_chave))

            with self.subTest(iteracao=i, texto=texto_aleatorio, chave=chave_aleatoria):
                cifrado = cifrar(texto_aleatorio, chave_aleatoria)
                decifrado = decifrar(cifrado, chave_aleatoria)

                # A mensagem decifrada deve ser idêntica à mensagem original (desconsiderando o padding final)
                self.assertEqual(
                    decifrado.rstrip(" "),
                    texto_aleatorio.rstrip(" "),
                    f"Falha na iteração {i}: texto='{texto_aleatorio}', chave='{chave_aleatoria}'"
                )

    def test_chaves_invalidas(self):
        """Garante que exceções de ValueError são lançadas para chaves sem letras."""
        chaves_invalidas = ["", "12345", "!@#$%", "   "]

        for chave in chaves_invalidas:
            with self.subTest(chave=chave):
                with self.assertRaises(ValueError):
                    cifrar("Mensagem de Teste", chave)


if __name__ == "__main__":
    unittest.main()