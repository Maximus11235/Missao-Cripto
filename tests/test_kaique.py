import unittest

from funcoes.Kaique import calcularPhi, expModular, teoremaChinesResto

class TestFuncoesKaique(unittest.TestCase):

    def test_calcular_phi(self):
        self.assertEqual(calcularPhi(10), 4)
        self.assertEqual(calcularPhi(36), 12)
        self.assertEqual(calcularPhi(97), 96) 
        
        with self.assertRaises(ValueError):
            calcularPhi(0)

    def test_exponenciacao_modular(self):
        self.assertEqual(expModular(5, 3, 13), 8)

    def test_teorema_chines_resto(self):
        self.assertEqual(teoremaChinesResto([2, 3], [3, 5]), 8)


if __name__ == "__main__":
    unittest.main()
