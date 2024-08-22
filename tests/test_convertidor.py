import unittest
from app import convertir_metros_a_kilometros, convertir_gramos_a_kilogramos, convertir_celsius_a_fahrenheit

class TestConvertidorUnidades(unittest.TestCase):

    def test_convertir_metros_a_kilometros(self):
        self.assertAlmostEqual(convertir_metros_a_kilometros(1000), 1.0)
        self.assertAlmostEqual(convertir_metros_a_kilometros(500), 0.5)
        self.assertAlmostEqual(convertir_metros_a_kilometros(0), 0.0)

    def test_convertir_gramos_a_kilogramos(self):
        self.assertAlmostEqual(convertir_gramos_a_kilogramos(1000), 1.0)
        self.assertAlmostEqual(convertir_gramos_a_kilogramos(500), 0.5)
        self.assertAlmostEqual(convertir_gramos_a_kilogramos(0), 0.0)

    def test_convertir_celsius_a_fahrenheit(self):
        self.assertAlmostEqual(convertir_celsius_a_fahrenheit(0), 32.0)
        self.assertAlmostEqual(convertir_celsius_a_fahrenheit(100), 212.0)
        self.assertAlmostEqual(convertir_celsius_a_fahrenheit(-40), -40.0)

if __name__ == '__main__':
    unittest.main()
