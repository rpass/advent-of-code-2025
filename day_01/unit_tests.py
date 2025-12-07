import unittest
from solution import process_input

class TestMyFunction(unittest.TestCase):
    def test_cases(self):
        test_cases = [
            ['simple_left', 'L1', 0],
            ['wrapping_left', 'L51', 1],
            ['simple_right', 'R1', 0]
        ]
        for name, input, expected_output in test_cases:
            print("subTest: ", name)
            with self.subTest(name=name):
                self.assertEqual(process_input(input), expected_output)

if __name__ == '__main__':
    unittest.main()