import unittest
from cifras.hill import encription_hill, decription_hill

class TestCifraHill(unittest.TestCase):

    def setUp(self):
        # Matriz 2x2
        # Determinante = (15 - 6) = 9. Inverso modular de 9 em mod 26 é 3.
        self.chave_valida = [[3, 3], [2, 5]]

    def test_cifragem_e_decifragem_bloco_exato(self):
        texto_original = "BOLA" # 4 letras, múltiplo de 2 (tamanho da chave)
        texto_cifrado = encription_hill(texto_original, self.chave_valida)
        texto_decifrado = decription_hill(texto_cifrado, self.chave_valida)
        
        self.assertEqual(texto_original, texto_decifrado)

    def test_preenchimento_padding_ultima_letra(self):
        texto_impar = "BOL" # 3 letras. O padding deve torná-lo "BOLL"
        texto_cifrado = encription_hill(texto_impar, self.chave_valida)
        texto_decifrado = decription_hill(texto_cifrado, self.chave_valida)
        
        self.assertEqual("BOLL", texto_decifrado)

if __name__ == "__main__":
    unittest.main()