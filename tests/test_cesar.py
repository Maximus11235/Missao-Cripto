import unittest
from cifras.cesar import encription_cesar, decription_cesar

class TestCifraCesar(unittest.TestCase):

    def test_cifragem_deslocamento_positivo(self):
        # Testa o comportamento padrão e o limite do alfabeto com salto 3
        self.assertEqual(encription_cesar("SECUREDOCS", 3), "VHFXUHGRFV")
        self.assertEqual(encription_cesar("ZIMBABWE", 3), "CLPEDEZH")

    def test_decifragem_deslocamento_positivo(self):
        # Garante que a operação inversa funciona corretamente
        self.assertEqual(decription_cesar("VHFXUHGRFV", 3), "SECUREDOCS")

    def test_cifragem_deslocamento_negativo(self):
        # Valida se o algoritmo suporta chaves negativas com salto -3
        self.assertEqual(encription_cesar("ALFA", -3), "XICX")

    def test_decifragem_deslocamento_negativo(self):
        self.assertEqual(decription_cesar("XICX", -3), "ALFA")
        
    def test_manutencao_de_espacos_e_caracteres_especiais(self):
        # Testa como a cifra lida com a mensagem interceptada
        mensagem = "TRANSFERIR DOCUMENTO"
        cifrado = encription_cesar(mensagem, 5)
        decifrado = decription_cesar(cifrado, 5)
        self.assertEqual(mensagem, decifrado)

if __name__ == "__main__":
    unittest.main()