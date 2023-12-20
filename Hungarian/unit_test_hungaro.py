import unittest
import pandas as pd
from io import StringIO
import sys
from methungaro import create_and_print_df  # assuming the function is in methungaro.py

class TestCreateAndPrintDF(unittest.TestCase):
    def setUp(self):
        self.data = [
        [50, 130, 190],
        [130, 100, 150],
        [110, 150, 270],
        [150, 90, 60]
    ]
        self.expected_output = """╔════════╦═════════════╦═════════════╦═════════════╦═════════════╗
║        ║   Columna 1 ║   Columna 2 ║   Columna 3 ║   Columna 4 ║
╠════════╬═════════════╬═════════════╬═════════════╬═════════════╣
║ Fila 1 ║           0 ║          40 ║         130 ║           0 ║
╠════════╬═════════════╬═════════════╬═════════════╬═════════════╣
║ Fila 2 ║          70 ║           0 ║          80 ║           0 ║
╠════════╬═════════════╬═════════════╬═════════════╬═════════════╣
║ Fila 3 ║          50 ║          50 ║         200 ║           0 ║
╠════════╬═════════════╬═════════════╬═════════════╬═════════════╣
║ Fila 4 ║         100 ║           0 ║           0 ║           0 ║
╚════════╩═════════════╩═════════════╩═════════════╩═════════════╝
"""

    def test_create_and_print_df(self):
        # Redirect stdout to a StringIO object
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        # Call the function
        create_and_print_df(self.data)

        # Reset stdout to its normal value
        sys.stdout = old_stdout

        # Assert that the function's output matches the expected output
        self.assertEqual(captured_output.getvalue().strip(), self.expected_output.strip())

if __name__ == '__main__':
    unittest.main()