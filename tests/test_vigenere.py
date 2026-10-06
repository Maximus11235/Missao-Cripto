import sys
from pathlib import Path

# Adiciona a pasta raiz do projeto ao caminho de busca do Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

import unittest
from cifras.vigenere import cifrar, decifrar

class TestCifraVigenere(unittest.TestCase):

    def test_cifragem_e_decifragem_basica(self):
        """Testa o funcionamento básico com texto simples e palavra-chave."""
        texto_original = "ATACAR"
        chave = "LIMAO"
        
        # Cifra e depois decifra o texto
        texto_cifrado = cifrar(texto_original, chave)
        texto_decifrado = decifrar(texto_cifrado, chave)
        
        # Garante que a mensagem decifrada é idêntica à original
        self.assertEqual(texto_decifrado, texto_original)

    def test_preservacao_de_casos_espacos_e_pontuacao(self):
        """Garante que letras maiúsculas/minúsculas, espaços e símbolos sejam mantidos."""
        texto_original = "Ataque ao Amanhecer as 05h!"
        chave = "senha"
        
        cifrado = cifrar(texto_original, chave)
        decifrado = decifrar(cifrado, chave)
        
        # O resultado decifrado deve ser exatamente igual ao texto original
        self.assertEqual(decifrado, texto_original)

    def test_chaves_invalidas(self):
        """Testa se o programa lança exceção ao receber chaves vazias ou sem letras."""
        with self.assertRaises(ValueError):
            cifrar("Mensagem", "")
            
        with self.assertRaises(ValueError):
            cifrar("Mensagem", "12345!@#")


# Executa os testes unitários caso o arquivo seja rodado diretamente
if __name__ == "__main__":
    unittest.main()