import unittest
from password_generator import generar_clave

class TestGeneradorContrasenas(unittest.TestCase):
    def test_longitud_por_defecto(self):
        self.assertEqual(len(generar_clave()), 12)

    def test_longitud_especifica(self):
        self.assertEqual(len(generar_clave(longitud=20)), 20)

    def test_inclusion_especiales(self):
        clave = generar_clave(incluir_especiales=True)
        tiene_especial = any(c in "!@#$%^&*()" for c in clave)
        self.assertTrue(tiene_especial)

    def test_exclusion_especiales(self):
        clave = generar_clave(incluir_especiales=False)
        tiene_especial = any(c in "!@#$%^&*()" for c in clave)
        self.assertFalse(tiene_especial)

if __name__ == '__main__':
    unittest.main()