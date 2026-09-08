import unittest

from funcoes.Andressa import (
    congruencia_linear,
    eh_primo,
    euclides_estendido,
    inverso_modular,
    mdc,
    mdc_recursivo,
    mod,
    mult_mod,
    pot_mod,
    sao_coprimos,
    soma_mod,
    sub_mod,
    totiente_euler,
)


class TestFuncoesAndressa(unittest.TestCase):
    def test_operacoes_modulares(self):
        self.assertEqual(mod(17, 5), 2)
        self.assertEqual(soma_mod(4, 5, 7), 2)
        self.assertEqual(sub_mod(2, 5, 7), 4)
        self.assertEqual(mult_mod(4, 5, 7), 6)
        self.assertEqual(pot_mod(3, 4, 5), 1)

    def test_euclides(self):
        self.assertEqual(mdc(48, 18), 6)
        self.assertEqual(mdc_recursivo(48, 18), 6)
        divisor, x, y = euclides_estendido(240, 46)
        self.assertEqual(divisor, 2)
        self.assertEqual(240 * x + 46 * y, divisor)

    def test_inverso_e_coprimalidade(self):
        self.assertEqual(inverso_modular(3, 11), 4)
        self.assertTrue(sao_coprimos(8, 15))
        with self.assertRaises(ValueError):
            inverso_modular(6, 15)

    def test_primalidade_e_totiente(self):
        self.assertTrue(eh_primo(97))
        self.assertFalse(eh_primo(1))
        self.assertEqual(totiente_euler(36), 12)

    def test_congruencia_linear(self):
        self.assertEqual(congruencia_linear(6, 9, 15), [4, 9, 14])
        self.assertEqual(congruencia_linear(4, 3, 6), [])


if __name__ == "__main__":
    unittest.main()
