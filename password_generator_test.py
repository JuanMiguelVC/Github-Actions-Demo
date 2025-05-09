import unittest
from password_generator import generar_clave, generar_multiples_claves


class TestGeneradorContrasenas(unittest.TestCase):
    def test_longitud_por_defecto(self):
        self.assertEqual(len(generar_clave(12)), 12)

    def test_longitud_especifica(self):
        self.assertEqual(len(generar_clave(20)), 20)

    def test_inclusion_especiales(self):
        clave = generar_clave(12, incluir_especiales=True)
        tiene_especial = any(c in "!@#$%^&*()" for c in clave)
        self.assertTrue(tiene_especial)

    def test_exclusion_especiales(self):
        clave = generar_clave(12, incluir_especiales=False)
        tiene_especial = any(c in "!@#$%^&*()" for c in clave)
        self.assertFalse(tiene_especial)

    def test_generar_multiples_claves(self):
        claves = generar_multiples_claves(3, 10)
        self.assertEqual(len(claves), 3)
        for clave in claves:
            self.assertEqual(len(clave), 10)

    def test_longitud_cero(self):
        with self.assertRaises(ValueError):
            generar_clave(0)

    def test_longitud_negativa(self):
        with self.assertRaises(ValueError):
            generar_clave(-5)
