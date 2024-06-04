from App import texto
import unittest

class TestCompararTextos(unittest.TestCase):
    def test_1(self):
        textoA = "Ruben"
        textoB = "Ruben"
        resul = texto(textoA, textoB)
    
        self.assertEqual(resul, True)
    def test_2(self):
        textoA = "12345"
        textoB = "Ruben"
        resul = texto(textoA, textoB)
        
        self.assertEqual(resul, False)


if __name__ == '__main__':
    unittest.main()
