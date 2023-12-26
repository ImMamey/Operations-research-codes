import unittest
from met_hunga import inicio
from parameterized import parameterized

"""
Caso 1: Ejercicio 1 de la lamina de hungaro
Caso 2: Ejercicio 2 de la lamina de hungaro
Caso 3: Primer ejercicio del siguiente link: https://www.estadistica.net/IO/Practica-Hungaro.pdf
Caso 4: Segundo ejercicio del siguiente link: https://www.estadistica.net/IO/Practica-Hungaro.pdf

"""


class TestHunga(unittest.TestCase):
    @parameterized.expand(
        [
            [
                "Caso 1",
                [[50, 130, 190],
                 [130, 100, 150],
                 [110, 150, 270],
                 [150, 90, 60]],
                [[3, 4], [1, 1], [2, 2], [4, 3]],
                210,"max"
            ],
            [
                "Caso 2",
                [[8, 7, 9, 8, 6],
                 [4, 5, 3, 5, 3],
                 [2, 3, 4, 3, 2],
                 [7, 6, 8, 6, 7],
                 [5, 4, 4, 6, 3]],
                [[3, 3], [1, 1], [4, 5], [5, 4], [2, 2]],
                30, "min"
            ],
            [
                "Caso 3",
                [[10, 9, 5],
                 [9, 8, 3],
                 [6, 4, 7]],
                [[2, 3], [1, 1], [3, 2]],
                17, "max"
            ],
            [
                "Caso 4",
                [[180, 150, 200, 200],
                 [250, 305, 450, 500],
                 [200, 208, 320, 100]],
                [[1, 2], [2, 1], [3, 4], [4, 3]],
                500, "max"
            ],
        ]
    )
    def test_sequence(self, _nombre, rest, expected_coors, expected_costo, f_o):
        result = inicio(rest,f_o)
        if result is not None and len(result) == 2:
            coors_result, costo_result = result
            self.assertEqual(coors_result, expected_coors)
            self.assertEqual(costo_result, expected_costo)
        else:
            self.assertTrue(
                result and len(result) == 2,
                "La funcion no devolvio el resultado esperado",
            )


if __name__ == "__main__":
    unittest.main()
