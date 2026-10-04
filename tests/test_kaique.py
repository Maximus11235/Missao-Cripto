import unittest

from funcoes.Kaique import (
    calcularPhi, 
    expModular, 
    teoremaChinesResto,
    multiplicar_matriz,
    determinante,
    adjunta
)

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

    def test_multiplicar_matriz(self):
        matriz_a = [[1, 2], [3, 4]]
        matriz_b = [[2, 0], [1, 2]]
        esperado = [[4, 4], [10, 8]]

        self.assertEqual(multiplicar_matriz(matriz_a, matriz_b), esperado)
        esperado_mod = [[4, 4], [0, 3]] 
        self.assertEqual(multiplicar_matriz(matriz_a, matriz_b, modulo=5), esperado_mod)      
        with self.assertRaises(ValueError):
            multiplicar_matriz([[1, 2]], [[1, 2]])

    def test_determinante(self):
        self.assertEqual(determinante([[1, 2], [3, 4]]), -2)
        self.assertEqual(determinante([[3, 3], [2, 5]]), 9) 

    def test_adjunta(self):
        matriz = [[3, 3], [2, 5]]
        esperado = [[5, -3], [-2, 3]]
        self.assertEqual(adjunta(matriz), esperado)

if __name__ == "__main__":
    unittest.main()
