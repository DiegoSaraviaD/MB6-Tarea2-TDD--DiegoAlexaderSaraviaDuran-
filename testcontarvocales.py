import unittest
from contarvocales import contar_vocales

class TestContarVocales(unittest.TestCase):
    def test_texto_con_vocales(self):
        self.assertEqual(contar_vocales("Hola Mundo"), 4)

    def test_texto_vacio(self):
        self.assertEqual(contar_vocales(""), 0)

if __name__ == "__main__":
    unittest.main()