import unittest

from funcoes.max import euclides_estendido, inverso_multiplicativo, eh_primo

class TestFuncoesMax(unittest.TestCase):

    def test_euclides_estendido(self):

        mdc_val, x, y = euclides_estendido(240, 46)
        self.assertEqual(mdc_val, 2)
        self.assertEqual(240 * x + 46 * y, mdc_val)

        mdc_val2, x2, y2 = euclides_estendido(35, 15)
        self.assertEqual(mdc_val2, 5)
        self.assertEqual(35 * x2 + 15 * y2, mdc_val2)

    def test_inverso_multiplicativo(self):
        self.assertEqual(inverso_multiplicativo(3, 11), 4)
        self.assertEqual(inverso_multiplicativo(7, 26), 15)

    def test_inverso_nao_existe(self):
        self.assertIsNone(inverso_multiplicativo(4, 8))

    def test_eh_primo(self):
        self.assertTrue(eh_primo(2))
        self.assertTrue(eh_primo(3))
        self.assertTrue(eh_primo(97))
        
        self.assertFalse(eh_primo(1))
        self.assertFalse(eh_primo(0))
        self.assertFalse(eh_primo(-5))
        self.assertFalse(eh_primo(4))
        self.assertFalse(eh_primo(35))


if __name__ == "__main__":
    unittest.main()
